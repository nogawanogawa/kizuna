<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-container fluid grid-list-lg pa-2>
            <v-layout>
              <v-flex xs12>
                <DetailBoard/>
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
import DetailBoard from "@/components/templates/DetailBoard.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    DetailBoard
  },
  props: {
    source: String
  },
  created() {
  }
};
</script>