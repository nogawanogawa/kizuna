<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex xs12>
            <UpdateBoard/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Sidebar from "@/components/templates/Sidebar.vue";
import UpdateBoard from "@/components/templates/UpdateBoard.vue";

export default {
  name: "SearchPage",
  components: {
    Sidebar,
    UpdateBoard
  },
  props: {
    source: String
  },
  created() {
  }
};
</script>