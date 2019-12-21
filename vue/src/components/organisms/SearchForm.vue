<template>
  <v-container fluid grid-list-xl>
    <v-layout wrap align-center>
      <v-flex xs10 offset-xs1>
        <v-btn block color="secondary" dark @click="searchall">Search</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
import { mapActions } from 'vuex'
export default {
  name: "SearchForm",
  methods: {
    ...mapActions(["searchall"])
  },
  data: () => ({
    items: ["A", "B", "C", "D"]
  })
};
</script>