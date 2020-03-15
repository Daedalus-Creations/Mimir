import '@babel/polyfill';
// Import Component hooks before component definitions
import './component-hooks';
import Vue from 'vue';
import './plugins/vuetify';
import './plugins/vee-validate';
import App from './App.vue';
import router from './router';
import store from '@/store';
import './registerServiceWorker';
import 'vuetify/dist/vuetify.min.css';
import Buefy from 'buefy';
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

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
