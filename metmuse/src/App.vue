<template>
  <div id="app">
    <StartSession v-if="!started" @sessionStarted="handleSessionStarted" />
    <Slider v-if="started" />
  </div>
</template>

<script>
import Slider from './components/Slider.vue';
import StartSession from './components/StartSession.vue';

export default {
  name: 'app',
  components: {
    Slider,
    StartSession,
  },
  data() {
    return {
      started: false,
    };
  },
  methods: {
    handleSessionStarted() {
      this.started = true;
    },
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  margin: 0px;
}
</style>
