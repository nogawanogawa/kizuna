<template>
  <v-container>
    <v-flex v-for="(item, i) in $store.state.items" :key="i">
      <ItemCard v-bind:title="item.title" v-bind:text="item.category" v-bind:index="item.index"></ItemCard>
    </v-flex>
  </v-container>
</template>

<script>
import ItemCard from "@/components/organisms/ItemCard.vue";
import { mapActions } from "vuex";

export default {
  name: "ItemPanel",
  components: {
    ItemCard
  },
  data: () => ({}),
  methods: {
    ...mapActions(["searchall"]),
    click() {
      this.$router.push({ path: "/Detail" });
    }
  },
  created() {
    this.searchall();
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>