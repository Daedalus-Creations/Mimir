import {IUserProfile, IQuote, IQuoteCreate, ITag} from '@/interfaces';

export interface AppNotification {
    content: string;
    color?: string;
    showProgress?: boolean;
}

export interface MainState {
    token: string;
    isLoggedIn: boolean | null;
    logInError: boolean;
    userProfile: IUserProfile | null;
    dashboardMiniDrawer: boolean;
    dashboardShowDrawer: boolean;
    notifications: AppNotification[];
    quotes: IQuote[];
    newQuote: IQuoteCreate;
    newQuoteOpen: boolean;
    tags: ITag[];
}
