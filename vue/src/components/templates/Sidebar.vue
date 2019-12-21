<template>
  <div>
    <v-app-bar app color="primary" dark clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="font-weight-black">Kizuna Dashboard</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item v-for="item in items" :key="item" @click="click(item.route)" class="white--text">
          <v-list-item-action>
            <v-icon>{{item.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{item.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>


<script>
export default {
  name: "Sidebar",
  data: () => ({
    drawer: null,
    items: [
      {
        icon: "home",
        text: "Home",
        route: "/Home"
      },
      {
        icon: "search",
        text: "Search",
        route: "/Search"
      },
      {
        icon: "insert_drive_file",
        text: "Register",
        route: "/Register"
      }
    ]
  }),
  methods: {
    click(route) {
      this.$router.push({ path: route });
    }
  }
};
</script>
