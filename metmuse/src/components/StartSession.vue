<template>
    <div class="start-session">
        <button class="center-button" @click="startSession">Start Session</button>
    </div>
</template>

<script>

export default {
  name: 'StartSession',

  props: {
    started: {
      type: Boolean,
      default: false,
    },
  },

  methods: {
    startSession() {
        console.log("here?")
        this.$emit('sessionStarted');
    }
  }
}

</script>
<style scoped>
.start-session {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #66999B;
  z-index: 9999;
}

.center-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 10px 20px;
  background-color: #ffffff; /* Set your desired button background color */
  color: #000000; /* Set your desired button text color */
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s; /* Add transition properties */
}

.center-button:hover {
  background-color: #394b4b; /* Set your desired hover background color */
  color: #d8d8d8; /* Set your desired hover text color */
}

</style>