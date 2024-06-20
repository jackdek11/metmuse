<template>
  <div>
    <transition-group name="fade" tag="div">
      <div v-for="i in [currentIndex]" :key="i">
        <img v-if="currentImg" :src="currentImg.file" style="object-fit: cover; height: 100%"/>
      </div>
    </transition-group>
    <a class="prev" @click="prev" href="#">&#10094; Previous</a>
    <a class="next" @click="next" href="#">&#10095; Next</a>
  </div>
</template>

<script>
import photosMixin from '@/mixins/calls'

export default {
  name: 'slider-component',
  data() {
    return {
      timer: null,
      currentIndex: 0,
      images: [],
      page: 1
    }
  },

  mounted: function () {
    this.startSlide()
    this.fillPhotos()
  },

  methods: {
    async fillPhotos() {
      try {
        let pictures = await photosMixin.getPhotos(this.page)
        this.images = this.images.concat(pictures.data.results)
        this.currentImg = this.pictures[this.index]
        this.network_errors = 0
      } catch (e) {
        this.index = 0
        this.page = Math.max(1, this.page - 1)
      }
    },
    startSlide: function () {
      this.timer = setInterval(this.next, 10000)
    },

    next: function () {
      this.currentIndex += 1
    },
    prev: function () {
      this.currentIndex -= 1
    }
  },

  watch: {
    currentIndex(newValue) {
      if (Math.abs(newValue) % this.images.length === 0) {
        this.page++
        this.fillPhotos()
      }
    }
  },

  computed: {
    currentImg: function () {
      if (this.images.length) {
        return this.images[Math.abs(this.currentIndex) % this.images.length]
      }
      return null
    }
  }
}
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.9s ease;
  overflow: hidden;
  visibility: visible;
  position: absolute;
  width: 100%;
  opacity: 1;
}

.fade-enter,
.fade-leave-to {
  visibility: hidden;
  width: 100%;
  opacity: 0;
}

img {
  object-fit: cover;
  height: 100%;
}

.prev,
.next {
  cursor: pointer;
  position: absolute;
  top: 40%;
  width: auto;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.7s ease;
  border-radius: 0 4px 4px 0;
  text-decoration: none;
  user-select: none;
}

.next {
  right: 0;
}

.prev {
  left: 0;
}

.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.9);
}
</style>
