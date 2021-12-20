<template>
    <div class="backdrop">
        <p class="close-text" @click="sendCreateRider">
            <i class="fas fa-times"></i>
        </p>
        <div class="row" >        
            <div class="col-md-2" ></div>
                <div class="col-md-8" >                   
                    <main class="mode container-lg">                          
                        <form class="row g-3" @submit.prevent="createRiders()">
                            <div class="col-md-6">
                                <label for="firstName" class="form-label">First Name</label>
                                <input type="text" class="form-control" id="firstName" v-model="firstName">
                            </div>
                            <div class="col-md-6">
                                <label for="inputPassword4" class="form-label">Last Name</label>
                                <input type="text" class="form-control" id="LastName" v-model="lastName">
                            </div>
                            <div class="col-md-6">
                                <label for="PhoneNumber" class="form-label">Phone Number</label>
                                <input type="text" class="form-control" id="PhoneNumber" v-model="phoneNumber" placeholder="Riders Personal Contact">
                            </div>
                            <div class="col-md-6">
                                <label for="CUGNumber" class="form-label">CUG Contact Number</label>
                                <input type="text" class="form-control" id="CUGNumber" v-model="CUGNumber" placeholder="Riders CUG Contact">
                            </div>
                            <div class="col-12">
                                <label for="inputAddress" class="form-label">Address </label>
                                <input type="text" class="form-control" id="inputAddress" v-model="Address">
                            </div>                            
                            <div class="col-12">
                                <label for="Select-vehicle" class="form-label">Select Vehicle</label>
                                <select id="Select-vehicle" class="form-select" v-model="attachedBike">
                                    <option selected>Choose...</option>
                                    <option v-for="item in ListFleets" :key="item.id" :value="item.id">
                                        {{ item.fleetPlateNumber}}, {{ item.vechileName  }}
                                    </option>
                                </select>
                            </div>                                                    
                            <div class="col-12">
                                <button type="submit" class="btn btn-primary" >Submit</button>
                            </div>
                        </form>                                                                                             
                    </main>
                </div>
            <div class="col-md-2" >
                {{ sendMessageError}}
            </div>
        </div>
    </div> 
</template>


<script>
import { computed, ref } from '@vue/reactivity'
import {  allFleets } from '../../graphql'
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'

export default {
    name:"OrdersToday",
    emits: ['CloseRidersForm'],

    setup(props, context){
        const sendCreateRider = () => {
            context.emit('CloseRidersForm')
        }
        const firstName = ref('')
        const lastName = ref('')
        const phoneNumber = ref('')
        const CUGNumber = ref('')
        const Address = ref('')
        const attachedBike = ref('')                   
        const ListFleets = computed(() => allFleets.value)
        const { mutate: createRiders, error: sendMessageError} = useMutation(gql`
            mutation createRiders( 
                $firstName: String!,
                $lastName: String!,
                $phoneNumber: String!,      
                $Address: String!,
                $attachedBike: Int!){ 
                
                   createRiders (
                    firstName: $firstName,
                    lastName: $lastName,
                    phoneNumber: $phoneNumber,     
                    Address: $Address,    
                    attachedBike: $attachedBike,
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
        `, () => ({
            variables: {
                firstName: firstName.value,
                lastName: lastName.value,
                phoneNumber: phoneNumber.value,
                Address: Address.value,
                attachedBike: attachedBike.value  
            },                         
        }))                      
    
        return {       
        sendCreateRider,
        firstName,
        lastName,
        phoneNumber,
        CUGNumber,
        Address,
        attachedBike,
        createRiders,
        ListFleets,        
        sendMessageError
        }
        
    }
    
}
</script>

<style scoped>
.mode {
    margin: auto;
    background-color: rgb(255, 255, 255);
    padding: 20px;
    height: 380px;
    overflow: scroll;    
}

.backdrop{
    top: 70px;
    position: fixed;
    right: 55px;
    background: rgba(0, 0, 0, 0.5);
    width: 75%;
    height: 510px;
    border-radius: 10px;
    padding: 10px;
}

.close-text{
    cursor: pointer;    
    color: rgb(255, 255, 238);
    width: fit-content;
    position: relative;
    left: 95%;
    font-size: 30px;
}


.mode::-webkit-scrollbar{
        width: 7px;
}

.mode::-webkit-scrollbar-track {
    border-radius: 50px;
}

.mode::-webkit-scrollbar-thumb {
    background-color: rgb(56, 110, 228);
    border-radius: 5px;
}

.mode::-webkit-scrollbar-thumb:hover {
    background-color: rgb(9, 38, 73);
}
</style>