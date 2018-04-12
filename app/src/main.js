import Vue from 'vue';
import App from './App.vue';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import fontawesome from '@fortawesome/fontawesome';
import faLightbulb from '@fortawesome/fontawesome-free-solid/faLightbulb';
import faMusic from '@fortawesome/fontawesome-free-solid/faMusic';
import VueCharts from 'vue-chartjs';
import {Bar, Line} from 'vue-chartjs';

fontawesome.library.add(faLightbulb);
fontawesome.library.add(faMusic);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
