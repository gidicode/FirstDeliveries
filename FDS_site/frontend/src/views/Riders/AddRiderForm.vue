<template>
    <div class="backdrop">
        <p class="close-text" @click="sendCreateRider">
            <i class="fas fa-times"></i>
        </p>
        <div class="row" >        
            <div class="col-md-2" ></div>
                <div class="col-md-8" >                   
                    <main class="mode container-lg">    
                        <small>Before creating a new riders you must have created a vehicle for the rider.</small>
                        <hr>
                        <form class="row g-3" @submit="onSubmit">
                            <div class="col-md-6">
                                <label for="firstName" class="form-label">First Name</label>
                                <input type="text" class="form-control" required id="firstName" v-model="firstName">
                                <span class="error-text">{{ firstNameError }}</span>
                            </div>
                            <div class="col-md-6">
                                <label for="inputPassword4" class="form-label">Last Name</label>
                                <input type="text" class="form-control" required id="LastName" v-model="lastName">
                                <span class="error-text">{{ lastNameError }}</span>
                            </div>
                            <div class="col-md-6">
                                <label for="PhoneNumber" class="form-label">Phone Number</label>
                                <input type="text" class="form-control" required id="PhoneNumber" v-model="phoneNumber" placeholder="Riders Personal Contact">
                                <span class="error-text">{{ PhoneNumberError }}</span>
                            </div>                           
                            <div class="col-md-6">
                                <label for="inputAddress" class="form-label">Address </label>
                                <input type="text" class="form-control" required id="inputAddress" v-model="Address">
                                <span class="error-text">{{ AddressError }}</span>
                            </div>                            
                            <div class="col-12">
                                <label for="Select-vehicle" class="form-label">Select Vehicle</label>
                                <select id="Select-vehicle" 
                                        class="form-select" 
                                        required 
                                        v-model="attachedBike"                                                                               
                                    >
                                        <option selected>Choose...</option>
                                        <template v-for="item in ListFleets" >
                                            <option :key="item.id" :value="item.id" v-if=" !item.attached ">                                           
                                                {{ item.fleetPlateNumber }}, {{ item.vechileName  }},  {{ item.attached }}                                            
                                            </option>                                            
                                        </template>
                                        
                                </select>
                            </div>                                                    
                            <div class="col-12">                                                             
                                <button class="btn btn-primary" type="button" v-if="sendMessageLoading">
                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                    Loading...
                                </button>
                                <button type="submit" class="btn btn-primary" v-else>Submit</button>                                
                            </div>
                        </form> 

                        <div class="submitSuccess" v-if="showSuccess">
                            <h6 class="text success">Submitted Successfuly</h6>                            
                        </div>

                         <div class="submitError" v-if="sendMessageError">
                            <h6 class="text-danger">an Error occured</h6>                            
                        </div>                       
                        
                    </main>
                </div>
            <div class="col-md-2" >                
            </div>
        </div>
    </div> 
</template>


<script>
    import { computed, ref } from '@vue/reactivity'
    import {  allFleets } from '../../graphql'
    import { useMutation } from '@vue/apollo-composable'
    import {useForm, useField} from 'vee-validate'
    import gql from 'graphql-tag'
    import * as yup from 'yup'           

    export default {
        name:"AddRiderForm",
        emits: ['CloseRidersForm'],

        setup(props, context){
            const sendCreateRider = () => {
                context.emit('CloseRidersForm')
            }                                                 
            const showSuccess = ref(false)
            const hideSuccess = () => showSuccess.value = !showSuccess

            const showError = ref(false)
            //const hideError = () => showError.value = !showError.value

            const schema = yup.object({
                phoneNumber: yup.string().required().min(11),                
                firstName: yup.string().required().max(50),
                lastName: yup.string().required().max(50),
                Address: yup.string().required().max(200),
                attachedBike: yup.string().required(),
            })
            useForm({
                validationSchema: schema,
            })
            const { handleSubmit } = useForm({
                validationSchema: schema,
            })
            const onSubmit = handleSubmit((values, {resetForm}) => {              
                createRiders()
                onDone(() => {                                      
                    console.log("hello")      
                     resetForm({
                    values: {
                        phoneNumber: '',
                        firstName: '',
                        lastName: '',
                        Address: '',
                        attachedBike: '',
                        }
                    })                                            
                })                                               
                                             
            })

            const {value: phoneNumber, errorMessage: PhoneNumberError} = useField('phoneNumber')
            const {value: firstName, errorMessage: firstNameError} = useField('firstName')
            const {value: lastName, errorMessage: lastNameError} = useField('lastName')
            const {value: Address, errorMessage: AddressError} = useField('Address')
            const {value: attachedBike, errorMessage: attachedBikeError} = useField('attachedBike')            

            const ListFleets = computed(() => allFleets.value)                        

            console.log(ListFleets.value)
                                
            const { mutate: createRiders, onDone, onError, error: sendMessageError, loading: sendMessageLoading} = useMutation(gql`
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
            
            onDone(() => {                                      
                showSuccess.value = !showSuccess.value
                showError.value = false
                setTimeout(hideSuccess, 5000)                
            }) 

            onError(({graphQLErrors, networkError}) => {
                if (graphQLErrors)
                    graphQLErrors.map(({message, locations, path}) => 
                        console.log(
                            `[GraphQL error]: Message: ${message}, 
                                            Location: ${locations},
                                            Path: ${path}`,                        
                        ),
                    )
                
                if (networkError) console.log(`[Network error]: ${networkError}`)
            })
            

            return {       
            sendCreateRider,
                        
            firstName,
            firstNameError,

            lastName,
            lastNameError,

            phoneNumber,
            PhoneNumberError,
        
            Address,
            AddressError,

            attachedBike,
            attachedBikeError,

            onSubmit,

            createRiders,
            
            ListFleets,      
            showSuccess,
            showError,
            sendMessageError,
            sendMessageLoading,
            
            }            
        }
        
    }
</script>


<style scoped>
.mode {
    margin: auto;
    background-color: rgb(255, 255, 255);
    padding: 40px;
    height: 380px;
    overflow: scroll; 
    border-top-left-radius: 20px;   
    border-bottom-left-radius: 20px;
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

.submitSuccess{
    background: rgb(198, 255, 184);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    position: absolute;
    top: 100px;
    right: 0;
    z-index: 1;
}

.submitError{
    background: rgb(255, 184, 184);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    position: absolute;
    top: 100px;
    right: 0;
    z-index: 1;
}

.error-text {
    font-size: 11px;
    color: red;
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