import gql from "graphql-tag"
import {provideApolloClient, useQuery, useResult} from '@vue/apollo-composable'
import { ApolloClient, InMemoryCache, createHttpLink} from '@apollo/client/core'


const cache = new  InMemoryCache()
const link = createHttpLink({uri: 'http://localhost:8000/graphql'})
const apolloClient  = new ApolloClient({   
    cache, link
})
provideApolloClient(apolloClient)


const {result} = useQuery(gql` 
      query GetallDeliveries{
          byCashDelivered {
            id                       
          }, 

          byErrandDelivered {
            id
          },

          byFrontDeskDelivered {
            id
          }, 

          byAllShopingDelivered {
            id
          },

          allCustomers {
          id
        },

      }
  `) 
export const paymentByCashDelivered = useResult(result, [], data => data.byCashDelivered)
export const errandDelivered = useResult(result, [], data => data.byErrandDelivered)
export const FrontDeskDelivered = useResult(result, [],  data => data.byFrontDeskDelivered)
export const shoppingDelivered = useResult(result, [], data => data.byAllShopingDelivered)
export const allPHcustomers = useResult(result, [], data => data.allCustomers)
