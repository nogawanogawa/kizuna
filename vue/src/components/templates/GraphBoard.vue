<template>
<v-layout>
<v-flex xs12>
    <Cytoscape />
</v-flex>
</v-layout>
</template>

<script>
import Cytoscape from "@/components/atoms/Cytoscape.vue";

export default {
  data() {
    return {};
  },
  components: {
    Cytoscape
  }
};
</script>


<style scoped>
.v-input__slider {
  width: 100%;
}
</style>