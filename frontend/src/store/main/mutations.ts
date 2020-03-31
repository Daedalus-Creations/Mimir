import {IUserProfile, IQuote, IQuoteCreate, defaultQuote, ITag} from '@/interfaces';
import {MainState, AppNotification} from './state';
import {getStoreAccessors} from 'typesafe-vuex';
import {State} from '../state';


export const mutations = {
  setToken(state: MainState, payload: string) {
    state.token = payload;
  },
  setLoggedIn(state: MainState, payload: boolean) {
    state.isLoggedIn = payload;
  },
  setLogInError(state: MainState, payload: boolean) {
    state.logInError = payload;
  },
  setUserProfile(state: MainState, payload: IUserProfile) {
    state.userProfile = payload;
  },
  setDashboardMiniDrawer(state: MainState, payload: boolean) {
    state.dashboardMiniDrawer = payload;
  },
  setDashboardShowDrawer(state: MainState, payload: boolean) {
    state.dashboardShowDrawer = payload;
  },
  addNotification(state: MainState, payload: AppNotification) {
    state.notifications.push(payload);
  },
  removeNotification(state: MainState, payload: AppNotification) {
    state.notifications = state.notifications.filter((notification) => notification !== payload);
  },
  setQuotes(state: MainState, payload: IQuote[]) {
    state.quotes = payload;
  },
  setQuote(state: MainState, payload: IQuote) {
    state.quotes[state.quotes.findIndex((quote)=> quote.id === payload.id)] = payload;
  },
  clearNewQuote(state: MainState){
    state.newQuote = Object.assign({}, defaultQuote);
  },
  setNewQuote(state: MainState, payload: IQuoteCreate) {
    state.newQuote = payload;
  },
  setNewQuoteOpen(state: MainState, payload: boolean){
    state.newQuoteOpen = payload;
  },
  setTags(state: MainState, payload: ITag[]){
    state.tags = payload;
  },
  setTag(state: MainState, payload: ITag){
    state.tags[state.tags.findIndex((tag)=> tag.id === payload.id)] = payload;
  }
};

const {commit} = getStoreAccessors<MainState | any, State>('');

export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
export const commitSetDashboardShowDrawer = commit(mutations.setDashboardShowDrawer);
export const commitSetLoggedIn = commit(mutations.setLoggedIn);
export const commitSetLogInError = commit(mutations.setLogInError);
export const commitSetToken = commit(mutations.setToken);
export const commitSetUserProfile = commit(mutations.setUserProfile);
export const commitAddNotification = commit(mutations.addNotification);
export const commitRemoveNotification = commit(mutations.removeNotification);
export const commitSetQuotes = commit(mutations.setQuotes);
export const commitSetQuote = commit(mutations.setQuote);
export const commitClearNewQuote = commit(mutations.clearNewQuote);
export const commitSetNewQuote = commit(mutations.setNewQuote);
export const commitSetNewQuoteOpen = commit(mutations.setNewQuoteOpen);
export const commitSetTags = commit(mutations.setTags);
export const commitSetTag = commit(mutations.setTag);