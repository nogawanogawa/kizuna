<template>
  <v-layout justify-center>
    <v-progress-circular v-if="display" indeterminate color="primary"></v-progress-circular>
  </v-layout>
</template>

<script>
export default {
  name: "ProgressCircle",
  props: {
    display: Boolean
  }
};
</script>

<style>
</style>
