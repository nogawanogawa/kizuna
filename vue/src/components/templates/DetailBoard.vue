<template>
  <v-card xs12 outlined flat>
    <v-card-title>{{property.title}}</v-card-title>
    <v-spacer></v-spacer>
    <DetailForm v-bind:property="property" />
    <v-card-actions>
      <v-container>
        <v-dialog v-model="dialog" persistent max-width="290">
          <template v-slot:activator="{ on }">
            <v-layout justify-end>
              <v-btn color="success" depressed @click="Update()">Update</v-btn>
              <v-btn color="error" depressed v-on="on">Delete</v-btn>
            </v-layout>
          </template>
          <v-card>
            <v-card-title class="headline">Delete</v-card-title>
            <v-card-text>削除しますか？</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="Delete();dialog = false">Yes</v-btn>
              <v-btn color="green darken-1" text @click="dialog = false">No</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
    </v-card-actions>
  </v-card>
</template>

<script>
import DetailForm from "@/components/organisms/DetailForm.vue";

export default {
  name: "DetailPanel",
  components: {
    DetailForm
  },
  data: () => ({
    dialog: false,
    property: {
      title: "Title",
      contents: "contents"
    }
  }),
  methods: {
    Update() {
      this.$router.push({ path: "/Update" });
    },
    Delete() {
      this.$router.push({ path: "/Delete" });
    }
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>