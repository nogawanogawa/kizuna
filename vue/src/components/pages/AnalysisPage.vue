<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex xs12>
            <GraphBoard/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Sidebar from "@/components/templates/Sidebar.vue";
import GraphBoard from "@/components/templates/GraphBoard.vue";

export default {
  name: "AnalysisPage",
  components: {
    Sidebar,
    GraphBoard
  },
  props: {
    source: String
  },
  created() {
  }
};
</script>