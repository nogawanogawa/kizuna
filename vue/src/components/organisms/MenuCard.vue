<template>
  <v-card :color="property.color" dark @click="click">
    <v-card-title>
      <v-icon x-large>{{property.icon}}</v-icon>
      {{property.title}}
    </v-card-title>
    <v-container>{{property.text}}</v-container>
  </v-card>
</template>

<script>
export default {
  name: "MenuCard",
  components: {},
  props: ["property"],
  data: () => ({}),
  methods: {
    click() {
      this.$router.push({ path: this.property.route });
    }
  }
};
</script>

<style scoped>
.v-input__slider {
  width: 100%;
}
</style>