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
import VueCharts from 'vue-chartjs';
import {Bar, Line} from 'vue-chartjs';

fontawesome.library.add(faLightbulb);
fontawesome.library.add(faMusic);
fontawesome.library.add(faLineChart);
fontawesome.library.add(faSave);
fontawesome.library.add(faCamera);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
}).$mount('#app');
