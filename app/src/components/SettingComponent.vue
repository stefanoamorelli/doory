<template lang='pug'>
 section.setting
  .setting__title.justify-content-center.align-items-center(:style="background")
   span {{ title }}
  .setting__body.d-flex.flex-column.justify-content-around
   .row
    .col
     span {{ body }}
   .row(v-show='title == "Settings"')
    .col-6
     label Name:
     input.form-control(v-model="firstname")
    .col-6
     label Conrad Connect:
     select.form-control(disabled )
      option(value='true') Enable
      option(value='false') Disable
    .col-6.mt-3
     label Doory speech:
     select.form-control(v-model='speech')
      option(value='true') Enable
      option(value='false') Disable
    .col-6.mt-3
     label Custom API:
     input.form-control(type='text')
    .col-12.mt-3.justify-content-end.d-flex
     .setting__icon.justify-content-center.align-items-center.save(@click='savedata()')
       i.fas.fa-save
   .row(v-if='title != "Settings"')
    .col-4.d-flex.flex-column.justify-content-center.align-items-center
     .setting__icon.justify-content-center.align-items-center
      i.fas.fa-chart-line
    .col-8.d-flex.flex-column.justify-content-center.align-items-center
     b You were {{ title }}:
     span {{ stats }} days
    .col-4.d-flex.flex-column.justify-content-center.align-items-center
     .setting__icon.justify-content-center.align-items-center
      i.fas.fa-music
    .col-8.d-flex.flex-column.justify-content-center.align-items-center
     b Select song: 
     select.form-control(v-model='song' @change='savedata')
      option(v-for='song in songs' :value='song') {{ song }}
   
</template>

<script>
import axios from 'axios';

var SONGS = ['Rock', 'NewAge', 'Pop', 'HipHop', 'Jazz'];

export default {
  props: ['title', 'image', 'body', 'stats'],
  components: {},
  data() {
    return {
      firstname: '',
      speech: '',
      song: '',
      songs: SONGS,
    };
  },
  computed: {
    background() {
      return 'background-image: url("' + this.image + '")';
    },
  },
  methods: {
    load() {
      if (this.title == 'Settings') {
        axios.get('http://188.166.111.117/doory/get_data.php').then(
          function(response) {
            this.firstname = response.data.name;
            this.speech = response.data.speech;
            console.log(response.data);
          }.bind(this),
        );
      } else {
        axios
          .get('http://188.166.111.117/doory/get_song_data.php?s=' + this.title)
          .then(
            function(response) {
              this.song = response.data;
              console.log(response.data);
            }.bind(this),
          );
      }
    },
    savedata() {
      if (this.title == 'Settings') {
        axios
          .post('http://188.166.111.117/doory/post_data.php', {
            name: this.firstname,
            speech: this.speech,
          })
          .then(function(response) {
            console.log(response.data);
          })
          .then(
            function() {
              this.load();
            }.bind(this),
          )
          .then(() => {
            alert('Settings saved!');
          });
      } else {
        axios
          .get(
            'http://188.166.111.117/doory/post_song_data.php?s=' +
              this.title +
              '&v=' +
              this.song,
          )
          .then(function(response) {
            console.log(response.data);
          })
          .then(
            function() {
              this.load();
            }.bind(this),
          )
          .then(() => {
            alert('Settings saved!');
          });
      }
    },
  },
  mounted() {
    this.load();
  },
};
</script>
<style lang='stylus' scoped>
.setting
 cursor -webkit-grab
 background white
 color gray
 border-radius 10px
 margin 50px 0
 box-shadow 0 0 70px 20px rgba(0,0,0,0.1) 
 transition all .5s ease
.setting:hover
 box-shadow 0 0 70px 10px rgba(0,0,0,0.1) 
 transform scale(1.05)
.setting__title
 background-size cover
 background-position center
 font-weight bolder
 text-transform uppercase
 border-radius 10px
 height 175px
 color white
 display flex
 font-size 3em
 position relative
 span
  z-index 1 
  opacity .9
.setting__title:before
 position absolute
 content " "
 top 0
 left 0
 width 100%
 height 100%
 display  block
 z-index 0
 background -moz-linear-gradient(top, rgba(0,0,0,0.81) 0%, rgba(0,0,0,0.65) 51%, rgba(82,82,82,0.5) 100%)
 background -webkit-linear-gradient(top, rgba(0,0,0,0.81) 0%,rgba(0,0,0,0.65) 51%,rgba(82,82,82,0.5) 100%)
 background linear-gradient(to bottom, rgba(0,0,0,0.81) 0%,rgba(0,0,0,0.65) 51%,rgba(82,82,82,0.5) 100%)
 border-radius 10px

.setting__body
 padding 30px
 min-height 320px
.setting__icon
 margin 10px
 width 60px
 height 60px
 font-size 2em
 background: rgb(0,123,255); /* Old browsers */
 background: -moz-linear-gradient(45deg, rgba(0,123,255,1) 0%, rgba(125,185,232,1) 100%); /* FF3.6-15 */
 background: -webkit-linear-gradient(45deg, rgba(0,123,255,1) 0%,rgba(125,185,232,1) 100%); /* Chrome10-25,Safari5.1-6 */
 background: linear-gradient(45deg, rgba(0,123,255,1) 0%,rgba(125,185,232,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
 border-radius 100%
 color white
 display flex
 
.save
 transition all .5s ease
 cursor pointer
.save:hover
 opacity .8

label
 font-size .8em
</style>
