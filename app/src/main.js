import Vue from 'vue';
import App from './App.vue';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import fontawesome from '@fortawesome/fontawesome';
import faLightbulb from '@fortawesome/fontawesome-free-solid/faLightbulb';
import faMusic from '@fortawesome/fontawesome-free-solid/faMusic';
import faLineChart from '@fortawesome/fontawesome-free-solid/faChartLine';
import faSave from '@fortawesome/fontawesome-free-solid/faSave';
import faCamera from '@fortawesome/fontawesome-free-solid/faCamera';
import faPause from '@fortawesome/fontawesome-free-solid/faPause';
import VueCharts from 'vue-chartjs';
import {Bar, Line} from 'vue-chartjs';

import VueAwesomeSwiper from 'vue-awesome-swiper';

fontawesome.library.add(faLightbulb);
fontawesome.library.add(faMusic);
fontawesome.library.add(faLineChart);
fontawesome.library.add(faSave);
fontawesome.library.add(faCamera);
fontawesome.library.add(faPause);

Vue.config.productionTip = false;

Vue.use(VueAwesomeSwiper);

new Vue({
  render: h => h(App),
}).$mount('#app');
