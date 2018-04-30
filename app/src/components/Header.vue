<template lang='pug'>
 section#header
  .container
   center
    .check
     i.fas.fa-camera
   h1 Doory
   .header__slogan.text-center Improving your mood, daily
   .small
    .mt-3.legend
     b Happiness chart
    Chart(:height="200")
  slot
</template>

<script>
import Chart from './Chart.js';
export default {
  components: {Chart},
  data() {
    return {};
  },
};
</script>

<style lang='stylus' scoped>
@import url('https://fonts.googleapis.com/css?family=Work+Sans:900');
@import url('https://fonts.googleapis.com/css?family=Lato:100i');
#header 
 min-height 100vh
 background: rgb(0,123,255); /* Old browsers */
 background: -moz-linear-gradient(45deg, rgba(0,123,255,1) 0%, rgba(125,185,232,1) 100%); /* FF3.6-15 */
 background: -webkit-linear-gradient(45deg, rgba(0,123,255,1) 0%,rgba(125,185,232,1) 100%); /* Chrome10-25,Safari5.1-6 */
 background: linear-gradient(45deg, rgba(0,123,255,1) 0%,rgba(125,185,232,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
 color var(--light)
 padding-top 30px
h1
 font-family 'Work Sans', sans-serif
 font-size 5em
 font-weight bolder
 text-align center
.header__slogan
 font-family 'Lato', sans-serif
 font-weight bolder
 font-size 2em
.legend
 padding 2px 5px
 border 1px solid white
 display table
 position absolute
 bottom 40px
 right 0
 font-size .8em
.small
 position relative
.check
 display flex
 align-items center
 justify-content center
 border 1px solid white
 border-radius 100%
 font-size 1.3em
 padding 15px
 width 70px
 height 70px
 font-size 2em
 transition all 1s ease
 cursor pointer
.check:hover
 transform scale(1.2)
 background white
 color #238cf9

</style>
