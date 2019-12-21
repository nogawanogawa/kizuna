import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        title: "",
        status: {
            success: false,
            error: false
        },
        category: "",
        content: "",
        index: "",
        display: {
            progress: false,
            alert: null
        },
        items: [
            {
                title: "Item 1",
                category: "Item 1",
                content: "Content1"
            },
            {
                title: "Item 2",
                category: "Item 2",
                content: "Content2"
            }
        ],
    },
    mutations: {
        create(state, json) {
            if (json.data.results) {
                state.status.success = true;
            } else {
                state.status.error = true;
            }
            state.display.progress = false
            state.title = json.data.results[0].title
            state.category = json.data.results[0].category
            state.content = json.data.results[0].content
        },
        searchall(state, json) {
            state.items = json.data.results
        },
        search(state, json) {
            state.index = json.data.results[0].index
            state.title = json.data.results[0].title
            state.category = json.data.results[0].category
            state.content = json.data.results[0].content
        },
        update(state, json) {
            state.index = json.data.results[0].index
            state.title = json.data.results[0].title
            state.category = json.data.results[0].category
            state.content = json.data.results[0].content
        },
        delete(state, json) {
            state.index = json.data.results[0].index
            state.title = json.data.results[0].title
            state.category = json.data.results[0].category
            state.content = json.data.results[0].content
        },
    },
    getters: {},
    actions: {
        create(ctx, json) {
            this.state.display.progress = true;
            this.state.status.success = false;
            this.state.status.error = false;
            axios
                .post('http://localhost:8080/create', json)
                .then(response => ctx.commit('create', response));
        },
        searchall(ctx) {
            axios
                .get('http://localhost:8080/read')
                .then(response => ctx.commit('searchall', response))
        },
        search(ctx, id) {
            axios
                .get('http://localhost:8080/read/' + JSON.stringify(id))
                .then(response => ctx.commit('search', response))
        },
        update(ctx, json) {
            axios
                .post('http://localhost:8080/update', json)
                .then(response => ctx.commit('update', response))
        },
        del(ctx, id) {
            axios
                .post('http://localhost:8080/delete', id)
                .then(response => ctx.commit('delete', response))
        }
    }
})

export default store