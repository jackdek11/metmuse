<script lang="ts">
import Burger from './icons/Burger.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      open: false
    }
  },
  mounted() {
    this.open
  },
  methods: {
    openMenu() {
      console.log("Test");
    }
  }
})
</script>

<template>
  <div class="wrapper">
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/login">Login</RouterLink>
    </nav>
  </div>
  <Burger @open="open"/>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
