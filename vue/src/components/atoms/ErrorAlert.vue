<template>
  <div>
    <v-alert
      v-model="display"
      border="left"
      close-text="Close Alert"
      color="error"
      dark
      dismissible
    >{{text}}</v-alert>
  </div>
</template>

<script>
export default {
  name: "ErrorAlert",
  data() {
    return {};
  },
  props: {
    display: Boolean,
    text: String
  }
};
</script>