<template>
  <v-card xs12 outlined flat>
    <v-card-title>Update</v-card-title>
    <v-spacer></v-spacer>
    <UpdateForm v-bind:property="property" />
    <ProgressCircle v-bind:display="$store.state.display.progress" />

    <v-container>
      <v-layout wrap justify-center align-center>
        <v-btn
          v-if="!$store.state.display.progress"
          color="secondary"
          dark
          @click="update(property)"
        >Update</v-btn>
      </v-layout>
      <SuccessAlert v-bind:display="$store.state.status.success" v-bind:text="success_msg" />
      <ErrorAlert v-bind:display="$store.state.status.error" v-bind:text="error_msg" />
    </v-container>
  </v-card>
</template>

<script>
import UpdateForm from "@/components/organisms/RegisterForm.vue";
import ProgressCircle from "@/components/atoms/ProgressCircle.vue";
import SuccessAlert from "@/components/atoms/SuccessAlert.vue";
import ErrorAlert from "@/components/atoms/ErrorAlert.vue";

export default {
  name: "DetailPanel",
  components: {
    UpdateForm,
    ProgressCircle,
    SuccessAlert,
    ErrorAlert
  },
  data: () => ({
    property: {
      title: "title",
      contents: "contents"
    }
  }),
  methods: {
    update(property) {
      this.$router.push({ path: "/Home/" + property });
    }
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>