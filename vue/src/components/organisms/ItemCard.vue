<template>
  <v-card color="blue-grey lighten-4"  flat>
    <v-card-text>
      <div class="headline mb-2">{{title}}</div>
      {{text}}
    </v-card-text>

    <v-card-actions>
      <v-btn text @click="search(index);click()">Detail</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "ItemCard",
  components: {},
  props: {
    title: String,
    text: String,
    index: String
  },
  data: () => ({}),
  methods: {
    ...mapActions(["search"]),
    click() {
      this.$router.push({ path: "/Detail" });
    }
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>