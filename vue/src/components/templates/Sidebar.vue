<template>
  <div>
    <v-app-bar app color="primary" dark clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="font-weight-black">Dashboard</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <v-list-item @click="click(items.home.route)" class="title">
          <v-list-item-action>
            <v-icon>{{items.home.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{items.home.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list-group
        v-for="parent in items.parent"
        :key="parent"
        @click="click(item.route)"
        class="title"
      >
        <template v-slot:activator>
          <v-list-item class="text">
            <v-list-item-action>
              <v-icon>{{parent.icon}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
                            <v-list-item-title>{{parent.text}}</v-list-item-title>

            </v-list-item-content>
          </v-list-item>
        </template>

        <v-list dense>
          <v-list-item
            v-for="child in parent.children"
            :key="child"
            @click="click(child.route)"
            class="white--text"
          >
            <v-list-item-action>
              <v-icon>{{child.icon}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{child.text}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-list-group>
    </v-navigation-drawer>
  </div>
</template>


<script>
export default {
  name: "Sidebar",
  data: () => ({
    drawer: null,
    items: {
      home: {
        icon: "home",
        text: "Home",
        route: "/Home"
      },
      parent: [
        {
          text: "Document",
          icon: "insert_drive_file",
          children: [
            {
              icon: "search",
              text: "Search",
              route: "/Search"
            },
            {
              icon: "insert_drive_file",
              text: "Register",
              route: "/Register"
            },
            {
              icon: "insert_chart_outlined",
              text: "Analysis",
              route: "/Analysis"
            }
          ]
        },
        {
          text: "Keyword",
          icon: "text_fields",
          children: [
            {
              icon: "search",
              text: "Keyword",
              route: "/Keyword"
            }
          ]
        }
      ]
    }
  }),
  methods: {
    click(route) {
      this.$router.push({ path: route });
    }
  }
};
</script>
