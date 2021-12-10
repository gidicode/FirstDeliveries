import { ApolloClient, InMemoryCache, createHttpLink} from '@apollo/client/core'

import { createApp, h, provide } from 'vue';
import { DefaultApolloClient } from '@vue/apollo-composable'
import App from "./App.vue";

const cache = new  InMemoryCache()
const link = createHttpLink({uri: 'http://localhost:8000/graphql'})
const apolloClient  = new ApolloClient({   
    cache, link
})

export const provider = apolloClient 
createApp({
    setup() {
      provide(DefaultApolloClient, apolloClient);
    },
  
    render() {
      return h(App);
    }
  }).mount('#app');