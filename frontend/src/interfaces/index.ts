export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IQuote {
    title: string;
    description?: string;
    public?: boolean;
    color?: string;
    tags?: Array<ITag>;
    id: number;
    owner_id: number;
}

export interface IQuoteUpdate {
    title?: string;
    description?: string;
    public?: boolean;
    color?: string;
    tags?: Array<ITag>;
}

export interface IQuoteCreate {
    title?: string;
    description?: string;
    public?: boolean;
    color?: string;
    tags?: Array<ITag>;
}

export interface ITag {
    title: string;
    public: boolean;
    color: string;
    id: number;
    owner_id: number;
}

export interface ITagCreate {
    title: string;
    public?: boolean;
    color?: string;
}

export interface ITagUpdate {
    title: string;
    public: boolean;
    color: string;
}