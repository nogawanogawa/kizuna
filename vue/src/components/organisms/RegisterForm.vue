<template>
  <v-container fluid grid-list-xl>
    <v-layout wrap align-center>
      <v-flex xs12 d-flex>
        <v-text-field v-model="property.title" label="Title" outlined></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout wrap align-center>
      <v-flex xs12 d-flex>
        <v-textarea v-model="property.contents" label="Contents" outlined></v-textarea>
      </v-flex>
    </v-layout>
  </v-container>
</template> 

<script>
import { mapActions } from "vuex";
export default {
  name: "RegisterForm",
  components: {
  },
  methods: {
    ...mapActions(["create"])
  },
  data: () => ({
  }),
  props: ["property"]
};
</script>