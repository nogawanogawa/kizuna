<template>
  <v-app id="inspire">
    <Sidebar />
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-container fluid grid-list-lg pa-2>
            <v-layout justify-center>
              <v-flex xs6>
                <v-text-field
                  v-model="search_word"
                  outlined
                  label="search"
                  append-icon="search"
                  @click:append="redirect(search_word)"
                  @keydown.enter="redirect(search_word)"
                ></v-text-field>
              </v-flex>
            </v-layout>
            <v-divider></v-divider>
            <v-layout>
              <v-flex xs12>
                <ItemBoard v-bind:items="items" />
              </v-flex>
            </v-layout>
          </v-container>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Sidebar from "@/components/templates/Sidebar.vue";
import ItemBoard from "@/components/templates/ItemBoard.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    ItemBoard
  },
  methods:{
    redirect(word){
      this.$router.push({
        path: this.path + "?" + "key=" + (word != null ? word : "")
      });
      this.$router.go({
        path: "",
        force: true
      })
    }
  },
  props: {
    source: String
  },
  data: () => ({
    search_word: "",
    path: "/Search"
  }),
  created() {}
};
</script>