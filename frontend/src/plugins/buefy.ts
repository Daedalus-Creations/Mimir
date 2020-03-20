import Buefy from 'buefy';
import Vue from 'vue';
import 'buefy/dist/buefy.css';
import { library } from '@fortawesome/fontawesome-svg-core';

// internal icons
import { faUser, faBook, faFeather, faEllipsisH, faGlobeAmericas, faComment, faQuoteRight, faFilm, faMusic, faExclamationCircle,
  faPlus, faStickyNote, faTrash, faExpand, faCompress, faCheck } from "@fortawesome/free-solid-svg-icons";
import {faEdit } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faUser, faBook, faFeather, faEllipsisH, faGlobeAmericas, faComment, faQuoteRight, faFilm, faMusic,
    faPlus, faEdit, faStickyNote, faTrash, faExpand, faCompress, faCheck, faExclamationCircle);
Vue.component('vue-fontawesome', FontAwesomeIcon);

// use buefy
Vue.use(Buefy, {
  defaultIconComponent: 'vue-fontawesome',
  defaultIconPack: 'fas',
});