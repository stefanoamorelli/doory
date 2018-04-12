<template lang='pug'>
  #app
   Header
   .container
    SettingComponent(v-for='mood in moods', :title='mood.title', :body='mood.body', :image='mood.image')
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
  },
  {
    title: 'Sorrow',
    body:
      "You feel sad, but I'm here to help. Select the best music and lighting for you to feel better.",
    image: 'https://www.todayschristianwoman.com/images/58926.jpg?w=620',
  },
  {
    title: 'Surprised',
    body: "Awesome news! Let's keep it beautiful with following settings:",
    image: 'https://upload.wikimedia.org/wikipedia/commons/0/0b/SURPRISE.jpg',
  },
  {
    title: 'Angry',
    body:
      'A day to forgot. Select the music and the lighting you like to make you relax.',
    image:
      'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjELehFnvjcJRp-IiGir67a3_GA9MLXkTfYPecX6lmEYaWoeBa',
  },
  {
    title: 'Neutral',
    body: 'Not bad, not good. How can we turn that day into a magical one?',
    image:
      'https://chopra.com/sites/default/files/field/image/on-again-off-again-meditating-does-it-do-any-good.jpg',
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
};
</script>

<style lang='stylus'>
</style>
