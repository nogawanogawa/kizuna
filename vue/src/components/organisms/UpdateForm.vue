<template>
  <v-container fluid grid-list-xl>
    <v-layout wrap align-center>
      <v-flex xs12 sm4 d-flex>
        <v-select :items="titles" v-model="title" label="Title" outlined></v-select>
      </v-flex>
      <v-flex xs12 sm4 d-flex>
        <v-select :items="categories" v-model="category" label="Category" outlined></v-select>
      </v-flex>
      <v-flex xs12 sm4 d-flex>
        <v-select :items="contents" v-model="content" label="Content" outlined></v-select>
      </v-flex>
      <v-flex xs10 offset-xs1>
        <v-btn
          v-if="!alert"
          block
          color="secondary"
          dark
          @click="update({'index':$store.state.index, 'title':title, 'category':category, 'content':content});click()"
        >Update</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template> 

<script>
import { mapActions } from "vuex";
export default {
  name: "UpdateForm",
  methods: {
    ...mapActions(["update"]),
    click() {
      alert("更新完了");
      this.$router.push({ path: "/Detail" });
    }
  },
  data() {
    return {
      titles: ["potato", "onion", "curry", "poak"],
      categories: ["food", "vagitable", "meat"],
      contents: ["good", "not good", "not bad", "bad"],
      alert: false
    };
  }
};
</script>