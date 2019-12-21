<template>
  <v-app id="inspire">
    <Sidebar/>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-container fluid grid-list-lg pa-2>
            <v-layout>
              <v-flex xs12>
                <RegisterBoard/>
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
import RegisterBoard from "@/components/templates/RegisterBoard.vue";

export default {
  name: "RegisterPage",
  components: {
    Sidebar,
    RegisterBoard
  },
  props: {
    source: String
  },
  created() {
  }
};
</script>