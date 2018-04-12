<template lang='pug'>
 section#header
  .container
   h1 Doory.
   .header__slogan.text-center Your happiness during previous months: 
   Chart
</template>

<script>
import Chart from './Chart.js';
export default {
  name: 'HelloWorld',
  components: {Chart},
  props: {
    msg: String,
  },
};
</script>

<style lang='stylus' scoped>
@import url('https://fonts.googleapis.com/css?family=Work+Sans:900');
@import url('https://fonts.googleapis.com/css?family=Lato:100i');
#header 
 background: rgb(0,123,255); /* Old browsers */
 background: -moz-linear-gradient(45deg, rgba(0,123,255,1) 0%, rgba(125,185,232,1) 100%); /* FF3.6-15 */
 background: -webkit-linear-gradient(45deg, rgba(0,123,255,1) 0%,rgba(125,185,232,1) 100%); /* Chrome10-25,Safari5.1-6 */
 background: linear-gradient(45deg, rgba(0,123,255,1) 0%,rgba(125,185,232,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
 color var(--light)
 padding 30px
h1
 font-family 'Work Sans', sans-serif
 font-size 5em
 font-weight bolder
 text-align center
.header__slogan
 font-family 'Lato', sans-serif
 font-weight bolder
 font-size 2em
</style>
