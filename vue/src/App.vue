<template>
  <router-view/>
</template>

<script>
export default {
  name: "app",
  data: () => ({
    drawer: null
  }),
  components: {},
  props: {
    source: String
  }
};
</script>