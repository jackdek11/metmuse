<template>
    <div class="start-session">
        <div class="clickable-area" @click="startSession">
            <!-- Image and content here -->
        </div>
        <div class="girl-onlooking">
            <!-- Image and content here -->
        </div>
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
  background-image: url('../assets/startup.png');
  height: 100%;
  background-color: #3b3939;
  background-position: center;
  background-repeat: no-repeat;
  background-size: fit;
  z-index: 9999;
}

.clickable-area {
  cursor: pointer;

}

.clickable-area::before {
  content: "";
  position: absolute;
  top: 40%;
  left: 40%;
  right: 37%;
  bottom: 40%;
}

.girl-onlooking::before {
  content: "";
  position: absolute;
  background-image: url('../assets/girl-2.png');
  background-position: center;
  background-repeat: no-repeat;
  background-size: 80%;
  background-size: fit;
  top: 40%;
  left: 12%;
  right: 67%;
  bottom: 0%;
}

</style>