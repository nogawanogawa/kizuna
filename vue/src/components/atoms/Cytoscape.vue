<template>
  <v-layout>
    <v-flex xs8>
      <v-card class="text" outlined>
        <div class="grapharea">
          <div id="cy"></div>
        </div>
      </v-card>
    </v-flex>
    <v-flex x4>
      <v-card class="text" outlined>
        <v-layout justify-center>
          <v-flex xs10>
            <v-text-field
              v-model="search_word"
              label="search"
              append-icon="search"
              @click:append="redirect(search_word)"
              @keydown.enter="redirect(search_word)"
            ></v-text-field>
          </v-flex>
        </v-layout>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
var cytoscape = require("cytoscape");

export default {
  name: "Cytoscape",
  components: {},
  created: function() {},
  data: function() {
    return {
      input: "",
      output: "",
      msg: "vue to cytoscape",
      count: 0,
      elements: {
        nodes: [
          { data: { id: "cat", name: "a" } },
          { data: { id: "bird" } },
          { data: { id: "ladybug" } },
          { data: { id: "aphid" } },
          { data: { id: "rose" } },
          { data: { id: "grasshopper" } },
          { data: { id: "plant" } },
          { data: { id: "wheat" } }
        ],
        edges: [
          { data: { source: "cat", target: "bird" } },
          { data: { source: "bird", target: "ladybug" } },
          { data: { source: "bird", target: "grasshopper" } },
          { data: { source: "grasshopper", target: "plant" } },
          { data: { source: "grasshopper", target: "wheat" } },
          { data: { source: "ladybug", target: "aphid" } },
          { data: { source: "aphid", target: "rose" } }
        ]
      }
    };
  },
  methods: {
    view_init: function() {
      this.cy = cytoscape({
        container: document.getElementById("cy"),
        boxSelectionEnabled: false,
        autounselectify: true,
        style: cytoscape
          .stylesheet()
          .selector("node")
          .css({
            height: 80,
            width: 80,
            "background-fit": "cover",
            "border-color": "#000",
            "border-width": 3,
            "border-opacity": 0.5,
            content: "data(name)",
            "text-valign": "center"
          })
          .selector("edge")
          .css({
            width: 6,
            "line-color": "#ffaaaa",
            "target-arrow-color": "#ffaaaa",
            "curve-style": "bezier"
          }),
        elements: this.elements,
        layout: {
          name: "circle",
          directed: true,
          padding: 10
        }
      });
      this.cy.on("tap", "node", function() {
          alert(this)
      })
    }
  },
  computed: {},
  mounted: function() {
    this.view_init();
  }
};
</script>
<style scoped>
#cy {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0px;
  left: 0px;
  text-align: left;
}
.grapharea {
  height: 700px;
}
body {
  font: 14px helvetica neue, helvetica, arial, sans-serif;
}
</style>