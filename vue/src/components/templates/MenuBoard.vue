<template>
  <v-container>
    <v-layout>
      <v-flex xs6 v-for="item in items" :key="item">
        <MenuCard v-bind:property="item" />
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
import MenuCard from "@/components/organisms/MenuCard.vue";

export default {
  name: "SearchPanel",
  components: {
    MenuCard
  },
  data: () => ({
    items: [
      {
        title: "DashBoard",
        text: "登録内容の分析",
        color: "deep-purple",
        icon: "bar_chart",
        route: "/Search"
      },
      {
        title: "Register",
        text: "文書の登録",
        color: "cyan",
        icon: "insert_drive_file",
        route: "/Register"
      },
      {
        title: "Search",
        text: "文書を探す",
        color: "primary",
        icon: "search",
        route: "/Search"
      }
    ]
  })
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>