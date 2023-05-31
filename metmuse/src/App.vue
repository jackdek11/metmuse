<template>
    <div class="display">
      <img v-bind:src=currentPicture.url v-if="currentPicture" style="object-fit: cover; height: 100%;">
    </div>
</template>

<script>
import photosMixin from '@/mixins/calls'

export default {
  name: 'App',
  methods: {
    async fillPhotos() {
      try{
        let pictures = await photosMixin.getPhotos(this.page);
        this.pictures = pictures.data.results;
        this.currentPicture = this.pictures[this.index];
      } catch (e) {
        this.page = 1;
        this.fillPhotos();
      }
    },
    setNextPicture() {
      if (this.pictures.length){
        this.index = (this.index + 1) % this.pictures.length;
      }
      if (this.index === 0){
        this.page++;
        this.fillPhotos();
      }
    },
    async countDownTimer() {
      if(this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 600)
      } else {
        setTimeout(async () => {
          this.setNextPicture();
          this.currentPicture = this.pictures[this.index];
          this.countDown = 10;
          this.countDownTimer();
        }, 600)
      }
    }
  },

  data() {
    return {
      countDown: 10,
      pictures: [],
      index: 0,
      page: 1,
      currentPicture: null
    }
  },

  created() {
    this.countDownTimer();
    this.fillPhotos();
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: C7CEDB;
}
.display {
  background-color: #2e3532;
  max-height: fit-content;
  height: 100%;
  justify-content: center;
  border-radius: 12px;
  min-height: 950px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
