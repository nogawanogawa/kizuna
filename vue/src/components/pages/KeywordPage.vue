<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-container fluid grid-list-lg pa-2>
            <v-layout>
              <v-flex xs12>
                <KeywordBoard/>
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
import KeywordBoard from "@/components/templates/KeywordBoard.vue";

export default {
  name: "RegisterPage",
  components: {
    Sidebar,
    KeywordBoard
  },
  props: {
    source: String
  },
  created() {
  }
};
</script>