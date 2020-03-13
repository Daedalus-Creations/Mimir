export enum type { BOOK='Book',
            FILM='Film',
            POEM='Poem',
            SPEECH='Speech',
            WEB='Web',
            LYRICS= 'Lyrics',
            OTHER='Other',
            UNCATEGORIZED='Uncategorized'}

export const typeIcon = {[type.BOOK]:'book',
                [type.FILM]:'film',
                [type.POEM]:'feather',
                [type.SPEECH]:'comments',
                [type.WEB]:'globe-americas',
                [type.LYRICS]: 'music',
                [type.OTHER]:'elipsis-h',
                [type.UNCATEGORIZED]:'quote-left'};

export const defaultQuote = {
                title: '',
                type: type.UNCATEGORIZED,
                text: '',
                description: '',
                public: false,
                color: '#2980B9',
                tags: [],
};

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
    type: type;
    text: string;
    description?: string;
    public?: boolean;
    color?: string;
    tags?: Array<ITag>;
    id: number;
    owner_id: number;
}

export interface IQuoteUpdate {
    title?: string;
    type?: type;
    text?: string;
    description?: string;
    public?: boolean;
    color?: string;
    tags?: Array<ITag>;
}

export interface IQuoteCreate {
    title?: string;
    type: type;
    text: string;
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