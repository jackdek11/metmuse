<template>
  <div>
    {{ picture }}
  </div>
</template>

<script>
export default {
  name: 'picture-detail',

  props: {
    picture: {
      type: Object,
      default: null
    }
  }
}
</script>
