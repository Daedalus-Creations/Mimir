import {api} from '@/api';
import router from '@/router';
import {getLocalToken, removeLocalToken, saveLocalToken} from '@/utils';
import {AxiosError} from 'axios';
import {getStoreAccessors} from 'typesafe-vuex';
import {ActionContext} from 'vuex';
import {State} from '../state';
import {
  commitAddNotification,
  commitRemoveNotification,
  commitSetLoggedIn,
  commitSetLogInError,
  commitSetToken,
  commitSetUserProfile,
  commitSetQuotes,
  commitSetTags,
} from './mutations';
import {AppNotification, MainState} from './state';
import {IQuote, IQuoteCreate, IQuoteUpdate, ITagUpdate, ITag} from '@/interfaces';

type MainContext = ActionContext<MainState, State>;

export const actions = {
  async actionLogIn(context: MainContext, payload: { username: string; password: string }) {
    try {
      const response = await api.logInGetToken(payload.username, payload.password);
      const token = response.data.access_token;
      if (token) {
        saveLocalToken(token);
        commitSetToken(context, token);
        commitSetLoggedIn(context, true);
        commitSetLogInError(context, false);
        await dispatchGetUserProfile(context);
        await dispatchRouteLoggedIn(context);
        commitAddNotification(context, {content: 'Logged in', color: 'success'});
      } else {
        await dispatchLogOut(context);
      }
    } catch (err) {
      commitSetLogInError(context, true);
      await dispatchLogOut(context);
    }
  },
  async actionGetUserProfile(context: MainContext) {
    try {
      const response = await api.getMe(context.state.token);
      if (response.data) {
        commitSetUserProfile(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateUserProfile(context: MainContext, payload) {
    try {
      const loadingNotification = {content: 'saving', showProgress: true};
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.updateMe(context.state.token, payload),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitSetUserProfile(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Profile successfully updated', color: 'success'});
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCheckLoggedIn(context: MainContext) {
    if (!context.state.isLoggedIn) {
      let token = context.state.token;
      if (!token) {
        const localToken = getLocalToken();
        if (localToken) {
          commitSetToken(context, localToken);
          token = localToken;
        }
      }
      if (token) {
        try {
          const response = await api.getMe(token);
          commitSetLoggedIn(context, true);
          commitSetUserProfile(context, response.data);
        } catch (error) {
          await dispatchRemoveLogIn(context);
        }
      } else {
        await dispatchRemoveLogIn(context);
      }
    }
  },
  async actionRemoveLogIn(context: MainContext) {
    removeLocalToken();
    commitSetToken(context, '');
    commitSetLoggedIn(context, false);
  },
  async actionLogOut(context: MainContext) {
    await dispatchRemoveLogIn(context);
    await dispatchRouteLogOut(context);
  },
  async actionUserLogOut(context: MainContext) {
    await dispatchLogOut(context);
    commitAddNotification(context, {content: 'Logged out', color: 'success'});
  },
  actionRouteLogOut(context: MainContext) {
    if (router.currentRoute.path !== '/login') {
      router.push('/login');
    }
  },
  async actionCheckApiError(context: MainContext, payload: AxiosError) {
    if (payload.response!.status === 401) {
      await dispatchLogOut(context);
    }
  },
  actionRouteLoggedIn(context: MainContext) {
    if (router.currentRoute.path === '/login' || router.currentRoute.path === '/') {
      router.push('/main');
    }
  },
  async removeNotification(context: MainContext, payload: { notification: AppNotification, timeout: number }) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        commitRemoveNotification(context, payload.notification);
        resolve(true);
      }, payload.timeout);
    });
  },
  async passwordRecovery(context: MainContext, payload: { username: string }) {
    const loadingNotification = {content: 'Sending password recovery email', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.passwordRecovery(payload.username),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Password recovery email sent', color: 'success'});
      await dispatchLogOut(context);
    } catch (error) {
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {color: 'error', content: 'Incorrect username'});
    }
  },
  async resetPassword(context: MainContext, payload: { password: string, token: string }) {
    const loadingNotification = {content: 'Resetting password', showProgress: true};
    try {
      commitAddNotification(context, loadingNotification);
      const response = (await Promise.all([
        api.resetPassword(payload.password, payload.token),
        await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
      ]))[0];
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {content: 'Password successfully reset', color: 'success'});
      await dispatchLogOut(context);
    } catch (error) {
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {color: 'error', content: 'Error resetting password'});
    }
  },
  async loadQuotes(context: MainContext) {
    try {
      const response = await api.getQuotes(context.state.token);
      if (response.data) {
        commitSetQuotes(context, response.data);
      }
    } catch (error) {
      throw error; // error handling
    }
  },
  async loadTags(context: MainContext) {
    try {
      const response = await api.getTags(context.state.token);
      if(response.data) {
        commitSetTags(context, response.data);
      }
    }
    catch(error){
      throw error;
    }
  },
  async updateQuote(context: MainContext, payload: IQuote) {
    try {
      let quote = JSON.parse(JSON.stringify(payload)) // clone payload
      delete quote.id; // remove id property
      delete quote.owner_id; // remove owner id property
      const quoteUpdate : IQuoteUpdate = quote; // verify with interface

      await api.updateQuote(context.state.token, payload.id, quoteUpdate);
    } catch (error) {
      throw error; // error handling
    }
  },
  async createQuote(context: MainContext, payload: IQuoteCreate) {
    try {
      await api.createQuote(context.state.token, payload);
    } catch (error) {
      throw error; // error handling
    }
  },
  async deleteQuote(context: MainContext, id : number) {
    try {
      await api.deleteQuote(context.state.token, id);
    } catch (error) {
      throw error; // error handling
    }
  },
  async updateTag(context: MainContext, payload: ITag) {
    try {
      let tag = JSON.parse(JSON.stringify(payload)) // clone payload
      delete tag.id; // remove id property
      delete tag.owner_id; // remove owner id property
      const tagUpdate : ITagUpdate = tag; // verify with interface

      await api.updateTag(context.state.token, payload.id, tagUpdate);
    } catch (error) {
      throw error; // error handling
    }
  },

};

const {dispatch} = getStoreAccessors<MainState | any, State>('');

export const dispatchCheckApiError = dispatch(actions.actionCheckApiError);
export const dispatchCheckLoggedIn = dispatch(actions.actionCheckLoggedIn);
export const dispatchGetUserProfile = dispatch(actions.actionGetUserProfile);
export const dispatchLogIn = dispatch(actions.actionLogIn);
export const dispatchLogOut = dispatch(actions.actionLogOut);
export const dispatchUserLogOut = dispatch(actions.actionUserLogOut);
export const dispatchRemoveLogIn = dispatch(actions.actionRemoveLogIn);
export const dispatchRouteLoggedIn = dispatch(actions.actionRouteLoggedIn);
export const dispatchRouteLogOut = dispatch(actions.actionRouteLogOut);
export const dispatchUpdateUserProfile = dispatch(actions.actionUpdateUserProfile);
export const dispatchRemoveNotification = dispatch(actions.removeNotification);
export const dispatchPasswordRecovery = dispatch(actions.passwordRecovery);
export const dispatchResetPassword = dispatch(actions.resetPassword);
export const dispatchLoadQuotes = dispatch(actions.loadQuotes);
export const dispatchLoadTags = dispatch(actions.loadTags);
export const dispatchUpdateQuote = dispatch(actions.updateQuote);
export const dispatchCreateQuote = dispatch(actions.createQuote);
export const dispatchDeleteQuote = dispatch(actions.deleteQuote);
export const dispatchUpdateTag = dispatch(actions.updateTag);
