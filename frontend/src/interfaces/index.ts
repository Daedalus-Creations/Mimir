export enum type {
    UNCATEGORIZED='Uncategorized',
    BOOK='Book',
    FILM='Film',
    POEM='Poem',
    SPEECH='Speech',
    WEB='Web',
    LYRICS= 'Lyrics',
    OTHER='Other'};

export const typeColor = new Map<string, string>([
  [type.BOOK, 'blue'],
  [type.FILM, 'red'],
  [type.POEM, 'pink'],
  [type.SPEECH, 'green'],
  [type.WEB, 'orange'],
  [type.LYRICS, 'teal'],
  [type.OTHER, 'indigo'],
  [type.UNCATEGORIZED, 'purple']]);

export const typeIcon = new Map<string, string>([
  [type.BOOK, 'book'],
  [type.FILM, 'film'],
  [type.POEM, 'feather'],
  [type.SPEECH, 'comment'],
  [type.WEB, 'globe-americas'],
  [type.LYRICS, 'music'],
  [type.OTHER, 'ellipsis-h'],
  [type.UNCATEGORIZED, 'quote-right']]);

export const defaultQuote: IQuoteCreate = {
  author: '',
  title: '',
  type: type.UNCATEGORIZED,
  text: '',
  description: '',
  public: false,
  color: null,
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
author: string;
title: string;
type: string;
text: string;
description?: string;
public?: boolean;
color?: string | null;
tags?: ITag[];
id: number;
owner_id: number;
}

export interface IQuoteUpdate {
author?: string;
title?: string;
type?: string;
text?: string;
description?: string;
public?: boolean;
color?: string | null;
tags?: ITag[];
}

export interface IQuoteCreate {
author?: string;
title?: string;
type: string;
text: string;
description?: string;
public?: boolean;
color?: string | null;
tags?: ITag[];
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
