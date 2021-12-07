import { createApp } from "vue";
import App from "./App.vue";

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import router from './router'

import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'

const httpLink = createHttpLink({
    url: 'http://localhost:8000/graphql',
})

const cache = new  InMemoryCache()

const apolloClient = new ApolloClient({
    link:httpLink,
    cache,
})

createApp(App).use(router, apolloClient).mount("#app");
