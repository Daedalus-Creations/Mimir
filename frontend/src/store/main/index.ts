import {mutations} from './mutations';
import {getters} from './getters';
import {actions} from './actions';
import {MainState} from './state';
import { defaultQuote } from '@/interfaces';

const defaultState: MainState = {
  isLoggedIn: null,
  token: '',
  logInError: false,
  userProfile: null,
  dashboardMiniDrawer: false,
  dashboardShowDrawer: false,
  notifications: [],
  quotes: [],
  newQuote: Object.assign({}, defaultQuote),
  newQuoteOpen: false,
  tags: [],
};

export const mainModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
