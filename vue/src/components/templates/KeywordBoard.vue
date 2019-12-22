<template>
  <v-card xs12 outlined flat>
    <v-card-title>
      Keyword
      <v-spacer></v-spacer>
      <v-layout>
        <v-flex xs6>
          <div class="text-center">
            <v-dialog v-model="dialog" width="500">
              <template v-slot:activator="{ on }">
                <v-btn color="primary" dark v-on="on" depressed>Add Word</v-btn>
              </template>
              <v-card>
                <v-card-title class="headline grey lighten-2" primary-title>Add word</v-card-title>

                <v-card-text>
                  <v-text-field v-model="word" label="word"></v-text-field>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" text @click="dialog = false">登録</v-btn>
                  <v-btn color="primary" text @click="dialog = false">キャンセル</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-flex>
        <v-flex xs6>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-card-title>
    <v-data-table :headers="headers" :items="desserts" :search="search">
      <template v-slot:item.delete="{ item }">
        <v-icon @click="del(item.word)">delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "KeywordBoard",
  methods: {
    del(word) {
      alert(word);
    }
  },
  data() {
    return {
      dialog: false,
      search: "",
      headers: [
        {
          text: "word",
          align: "left",
          sortable: false,
          value: "word"
        },
        { text: "delete", value: "delete" }
      ],
      desserts: [
        {
          word: "Frozen Yogurt"
        },
        {
          word: "Ice cream sandwich"
        },
        {
          word: "Eclair"
        },
        {
          word: "Cupcake"
        },
        {
          word: "Gingerbread"
        },
        {
          word: "Jelly bean"
        },
        {
          word: "Lollipop"
        },
        {
          word: "Honeycomb"
        },
        {
          word: "Donut"
        },
        {
          word: "KitKat"
        }
      ]
    };
  }
};
</script>
<style scoped>
.v-input__slider {
  width: 100%;
}
</style>