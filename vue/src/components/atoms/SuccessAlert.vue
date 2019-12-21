<template>
  <div>
    <v-alert
      v-model="display"
      border="left"
      close-text="Close Alert"
      color="success"
      dark
      dismissible
    >{{text}}</v-alert>
  </div>
</template>

<script>
export default {
  name: "SuccessAlert",
  data() {
    return {};
  },
  props: {
    display: Boolean,
    text: String
  }
};
</script>