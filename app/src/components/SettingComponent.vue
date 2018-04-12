<template lang='pug'>
 section.setting
  .setting__title.justify-content-center.align-items-center(:style="background")
   span {{ title }}
  .setting__body.d-flex.flex-column.justify-content-around
   .row
    .col
     span {{ body }}
   .row
    .col.d-flex.flex-column.justify-content-center.align-items-center
     .setting__icon.justify-content-center.align-items-center
      i.fas.fa-music
    .col.d-flex.flex-column.justify-content-center.align-items-center
     .setting__icon.justify-content-center.align-items-center
      i.fas.fa-lightbulb
   .row
    .col.d-flex.flex-column.justify-content-center.align-items-center
     select.form-control
      option(v-for='playlist in playlists') {{ playlist }}
    .col.d-flex.flex-column.justify-content-center.align-items-center
     select.form-control
      option(v-for='light in lights') {{ light }}

   
</template>

<script>
var PLAYLISTS = ['Rock', 'Pop', 'New age', 'Jazz'];
var LIGHTS = ['Green', 'Blue', 'Yellow', 'Red'];
export default {
  props: ['title', 'image', 'body'],
  components: {},
  data() {
    return {
      lights: LIGHTS,
      playlists: PLAYLISTS,
    };
  },
  computed: {
    background() {
      return 'background-image: url("' + this.image + '")';
    },
  },
};
</script>
<style lang='stylus' scoped>
.setting
 color gray
 border-radius 10px
 margin 50px 0
 box-shadow 0 0 50px 10px #eee
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
 height 300px
.setting__icon
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
 
</style>
