<template lang='pug'>
  #app
   Header
    #pages
     .dragend-page
      SettingComponent(title='Settings' body='' image='https://www.growly.io/wp-content/uploads/2016/08/15-must-have-tools-for-small-business.jpg')
     .dragend-page(v-for='mood in moods')
      SettingComponent(:title='mood.title' :body='mood.body' :image='mood.image' :stats='mood.stats')
</template>

<script>
import Header from './components/Header.vue';
import SettingComponent from './components/SettingComponent.vue';

var MOODS = [
  {
    title: 'Happy',
    body:
      'A beautiful day! We can make it even better, with the music you like and the lighthing you prefer.',
    image:
      'http://positivepsychology.org.uk/wp-content/uploads/2008/11/eygnomosyni_1-min.jpg',
    stats: '102',
  },
  {
    title: 'Sorrow',
    body:
      "You feel sad, but I'm here to help. Select the best music and lighting for you to feel better.",
    image: 'https://www.todayschristianwoman.com/images/58926.jpg?w=620',
    stats: '2',
  },
  {
    title: 'Surprised',
    body: "Awesome news! Let's keep it beautiful",
    image: 'https://upload.wikimedia.org/wikipedia/commons/0/0b/SURPRISE.jpg',
    stats: '30',
  },
  {
    title: 'Angry',
    body:
      'A day to forgot. Select the music and the lighting you like to make you relax.',
    image:
      'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjELehFnvjcJRp-IiGir67a3_GA9MLXkTfYPecX6lmEYaWoeBa',
    stats: '50',
  },
  {
    title: 'Neutral',
    body: 'Not bad, not good. How can we turn that day into a magical one?',
    image:
      'https://chopra.com/sites/default/files/field/image/on-again-off-again-meditating-does-it-do-any-good.jpg',
    stats: '125',
  },
];

export default {
  name: 'app',
  components: {
    Header,
    SettingComponent,
  },
  data() {
    return {
      moods: MOODS,
    };
  },
  mounted() {
    new Dragend(document.getElementById('pages'));
  },
};
</script>

<style lang='stylus'>
.dragend-page
 padding 30px !important
#pages
 height 700px
#pages > div
 transform translateX(-2550px)
 transition all 3.5s ease
</style>
