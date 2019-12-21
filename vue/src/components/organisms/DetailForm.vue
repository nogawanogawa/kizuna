<template>
  <v-container fluid grid-list-xl>
    <v-layout>
      <v-flex>{{property.contents}}</v-flex>
    </v-layout>
  </v-container>
</template> 

<script>
export default {
  name: "DetailForm",
  data: () => ({}),
  props: ["property"]
};
</script>