import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  mounted () {
    this.renderChart({
    labels: ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.'],
      datasets: [
        {
          fill: false,
          borderColor: "#fff",
          backgroundColor: '#fff',
          data: [10, 16, 12, 17, 16, 20, 12, 15,10, 23, 20]
        }
      ]
      }, { legend: { display: false }, elements: { point: { radius: 0 } } , scales: { xAxes: [{ ticks: { fontColor:'white'},  gridLines: { display: false, drawBorder: false } }], yAxes: [{ ticks: { display: false, beginAtZero: true}, gridLines: { display:false, drawBorder: false } }]}})
  }
}
