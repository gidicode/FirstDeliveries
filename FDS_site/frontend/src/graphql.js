import gql from "graphql-tag"
import {provideApolloClient, useQuery, useResult} from '@vue/apollo-composable'
import { ApolloClient, InMemoryCache, createHttpLink} from '@apollo/client/core'
import { onError } from '@apollo/client/link/error'
import { logErrorMessages } from '@vue/apollo-util'

const errorlink = onError(error => {
  logErrorMessages(error)
})

const cache = new  InMemoryCache()
const link = createHttpLink({uri: 'http://localhost:8000/graphql'})
const apolloClient  = new ApolloClient({   
    cache, link: errorlink.concat(link)
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

          byAllShoppingDelivered {
            id
          },

          allCustomers {
            id            
            firstName
            lastName
            user{
              id
              username
              dateJoined
            }
            email
            phoneNumber
            AltPhoneNum           
          },

          allFleets {
            id
            fleetPlateNumber
            vechileName
            attached       
          },

          allRiders {
            id
          },

          byCashPending {
            id
          },

          byErrandPending {
            id
          },

          byFrontDeskPending {
            id
          },

          byAllShoppingPending {
            id
          },

          allFrontDesk {
            id
          },

          allContact {
            id
          },

          byCashDate {
            id
            customer {
              firstName
              lastName
              phoneNumber
            }
            dateCreated
            status
          },

          byErrandDate {
            id
            customer {
              firstName
              lastName
              phoneNumber
            }
            dateCreated
            status
          },

          byFrontDeskDate {
            id
            CustomerPhoneNumber
            RecieverPhoneNumber
            dateCreated
            status
          },

          byAllShoppingDate {
            id
            customer {
              firstName
              lastName
              phoneNumber
            }
            dateCreated
            status
          },

        }
    `,null, {
        pollInterval: 1000,
    }) 



/*  
export const { mutate: createRiders } = useMutation(gql`
  mutation createRiders (      
      $firstName: String!,
      $lastName: String!,
      $PhoneNumber: String!,      
      $inputAddress: String!,
      $SelectVehicle: String!
    ){
    createRiders(          
      firstName: $firstName,
      lastName: $lastName,
      phoneNumber: $PhoneNumber,     
      Address: $inputAddress,    
      attachedBike: $SelectVehicle,    
    ){
      riders {
        id      
        firstName
        lastName
        phoneNumber    
        Address
        attachedBike {
          id
          TrackerId
          TrackerPhoneNum
          dateCreated        
        }
      }
    } 
  }
`)
console.log(createRiders)
*/
export const paymentByCashDelivered = useResult(result, [], data => data.byCashDelivered)
export const errandDelivered = useResult(result, [], data => data.byErrandDelivered)
export const FrontDeskDelivered = useResult(result, [],  data => data.byFrontDeskDelivered)
export const shoppingDelivered = useResult(result, [], data => data.byAllShoppingDelivered)

//Customers
export const allPHcustomers = useResult(result, [], data => data.allCustomers)

//RIDERS AND FLEET INFO
export const allRiders = useResult(result, [], data => data.allRiders)
export const allFleets = useResult(result, [], data => data.allFleets)

//Pending deliveries
export const byCashPending = useResult(result, [], data => data.byCashPending)
export const byErrandPending = useResult(result, [], data => data.byErrandPending)
export const byFrontDeskPending = useResult(result, [], data => data.byFrontDeskPending)
export const byAllShoppingPending = useResult(result, [], data => data.byAllShoppingPending)

//allFrontDesk
export const allFrontDesk = useResult(result, [], data => data.allFrontDesk)

//AllContact
export const allContact = useResult(result, [], data => data.allContact)

//FilterByTime
export const cashDateToday = useResult(result, [], data => data.byCashDate)
export const errandDateToday = useResult(result, [], data => data.byErrandDate)
export const frontDeskDateToday = useResult(result, [], data => data.byFrontDeskDate)
export const shoppingDateToday = useResult(result, [], data => data.byAllShoppingDate)
