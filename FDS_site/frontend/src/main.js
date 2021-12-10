import { createApp, h, provide } from "vue";
import App from "./App.vue";
import router from './router'
import { ApolloClient, InMemoryCache, createHttpLink} from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"


//const app = createApp(App)
//app.use(router)
//app.mount('#app')

const cache = new  InMemoryCache()
const link = createHttpLink({uri: 'http://localhost:8000/graphql'})
const apolloClient  = new ApolloClient({   
    cache, link
})

createApp({App, 
    setup() {
        provide(DefaultApolloClient, apolloClient);
      },

      render() {
        return h(App);
      }
}).use(router).mount('#app')



