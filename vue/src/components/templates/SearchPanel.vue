<template>
  <v-card xs12 color="grey darken-2">
    <v-card-title>Search</v-card-title>
    <v-spacer></v-spacer>
    <SearchForm/>
  </v-card>
</template>

<script>
import SearchForm from "@/components/organisms/SearchForm.vue";

export default {
  name: "SearchPanel",
  components: {
    SearchForm
  },
  data: () => ({})
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>