<template>
  <v-container>
    <p class="headline">Document</p>
    <v-layout>
      <MenuCard v-for="item in document" :key="item" v-bind:property="item" />
    </v-layout>

    <p class="headline">Word</p>
    <v-layout>
      <MenuCard v-for="item in word" :key="item" v-bind:property="item" />
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
    document: [
      {
        title: "DashBoard",
        text: "登録内容の分析",
        color: "deep-purple",
        icon: "bar_chart",
        route: "/Analysis"
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
    ],
    word: [
      {
        title: "Keyword",
        text: "単語の操作",
        color: "deep-purple",
        icon: "text_fields",
        route: "/Keyword"
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