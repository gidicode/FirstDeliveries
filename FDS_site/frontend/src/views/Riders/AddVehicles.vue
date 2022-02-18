<template>
    <div class="backdrop">
        <p class="close-text" @click="sendCreateVehicle">
            <i class="fas fa-times"></i>
        </p>
        <div class="row" >        
            <div class="col-md-2" ></div>
                <div class="col-md-8" >                   
                    <main class="mode container-lg">                          
                        <form class="row g-3" @submit.prevent="onSubmit">
                            <div class="col-md-6">
                                <label for="plateNumber" class="form-label">Plate Number</label>
                                <input type="text" class="form-control" required id="plateNumber" v-model="fleetPlateNumber">
                                <span class="error-text">{{ fleetPlateNumberError }}</span>
                            </div>
                            <div class="col-md-6">
                                <label for="trackerId" class="form-label">Tracker Id</label>
                                <input type="text" class="form-control" required id="trackerId" v-model="TrackerId">
                                <span class="error-text">{{ TrackerIdError }}</span>
                            </div>
                            <div class="col-md-6">
                                <label for="trackerPhoneNumber" class="form-label">Tracker Phone Number</label>
                                <input type="text" class="form-control" required id="trackerPhoneNumber" v-model="TrackerPhoneNum" placeholder="Contact inside tracker">
                                <span class="error-text">{{ TrackerPhoneNumError }}</span>
                            </div>                           
                            
                            <div class="col-md-6">
                                <label for="vechileName" class="form-label">Vehicle Name</label>
                                <input type="text" class="form-control" required id="vechileName" v-model="vechileName" placeholder="Brief Description of vehicle">
                                <span class="error-text">{{ vechileNameError }}</span>
                            </div>  
                                                                                     
                            <div class="col-12">
                                <label for="category" class="form-label">Category </label>
                                <select id="category" class="form-select" required v-model="category">
                                    <option selected>Choose...</option>
                                     <option >Bike</option>
                                     <option >Tricycle</option>
                                     
                                </select>
                                <span class="error-text">{{ categoryError }}</span>
                            </div>                  

                            <div class="col-12"> 
                                <button class="btn btn-primary" type="button" v-if="sendMessageLoading">
                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                    Loading...
                                </button>
                                <button type="submit" class="btn btn-primary" v-else>Submit</button>                                
                            </div>

                            <div class="submitSuccess" v-if="showSuccess">
                                <h6 class="text success">Submitted Successfuly</h6>                            
                            </div>

                            <div class="submitError" v-if="sendMessageError">
                                <h6 class="text-danger">an Error occured</h6>                            
                            </div>  
                        </form>                                                                                             
                    </main>
                </div>
            <div class="col-md-2" >                
            </div>
        </div>
    </div> 
</template>


<script>
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { ref } from '@vue/reactivity'
import {useForm, useField} from 'vee-validate'
import * as yup from 'yup'   

export default {
    name:"AddVehicles",
    emits: ['CloseVehicleForm'],

    setup(props, context){
        const sendCreateVehicle = () => {
            context.emit('CloseVehicleForm')
        } 

        const showSuccess = ref(false)
        const hideSuccess = () => showSuccess.value = !showSuccess

        const showError = ref(false)

        const schema = yup.object({
            fleetPlateNumber: yup.string().required().max(11).min(11),
            TrackerId: yup.string().required(),
            category: yup.string().required(),
            vechileName: yup.string().required(),
            TrackerPhoneNum: yup.string().required().min(11).max(11),
        })        
        
        const { handleSubmit, setFieldError } =  useForm({
            validationSchema: schema,
        })  

        const onSubmit = handleSubmit((values, { resetForm, setFieldError}) => {            
            createFleet()

            onDone(() => {                
                resetForm({
                    values: {
                    fleetPlateNumber: '',
                    TrackerId: '',
                    category: '',
                    vechileName: '',
                    TrackerPhoneNum: '',
                    
                    },                                   
                })

                setFieldError( 'TrackerIdError', '')               
            })
            
        })

        const { value: fleetPlateNumber, 
                errorMessage:fleetPlateNumberError
              } = useField('fleetPlateNumber')

        const { value: TrackerId, errorMessage: TrackerIdError} = useField('TrackerId')
        const { value: category, errorMessage: categoryError} = useField('category')
        const { value: vechileName, errorMessage:vechileNameError} = useField('vechileName')

        const { value: TrackerPhoneNum, 
                errorMessage:TrackerPhoneNumError 
              } = useField('TrackerPhoneNum')

        const {mutate: createFleet, onDone, onError, error: sendMessageError, loading: sendMessageLoading } = useMutation(gql`
            mutation createFleet(
                $fleetPlateNumber: String!,
                $TrackerId: String!,
                $TrackerPhoneNum: String!,
                $category: String!,
                $vechileName:String!
                $dateCreated: DateTime! 
                ){
                createFleet (
                    fleetPlateNumber:$fleetPlateNumber,
                    TrackerId: $TrackerId,
                    TrackerPhoneNum: $TrackerPhoneNum,
                    category: $category,
                    vechileName: $vechileName,
                    dateCreated: $dateCreated,
                ){
                    fleet {
                        id 
                        fleetPlateNumber
                        TrackerId
                        TrackerPhoneNum
                        category
                        vechileName
                        dateCreated
                    }
                }    
            }
        `, () => ({
                variables: {
                    fleetPlateNumber: fleetPlateNumber.value,
                    TrackerId: TrackerId.value,
                    TrackerPhoneNum: TrackerPhoneNum.value,
                    category: category.value,
                    vechileName: vechileName.value,
                    dateCreated: new Date()
                },                
            }),            
        )

        onDone(() => {
            console.log("done")
            showSuccess.value = !showSuccess.value
            showError.value = false
            setTimeout(hideSuccess, 5000)
        })

        onError(({graphQLErrors}) => {
            if(graphQLErrors)
                graphQLErrors.map(({ message, locations, path}) =>                     
                console.log(`[GraphQL error]: Message: ${message}, 
                            Location: ${locations}, path: ${path}`),                            
                )

                const getMessage = graphQLErrors.map(({message}) => `${message}`)
                    console.log(getMessage[0], 'alright')                    

                const MessagePhoneNumber = "UNIQUE constraint failed: PortHarcourt_fleets_ph.Tracker_phone_num"
                const MessageTrackerId = "UNIQUE constraint failed: PortHarcourt_fleets_ph.Tracker_id"
                const MessagePlateNumber = "UNIQUE constraint failed: PortHarcourt_fleets_ph.fleet_plate_number"

                if (getMessage[0] == MessagePhoneNumber) {
                    setFieldError('TrackerPhoneNum', 'Phone Number is Already assigned!')
                }

                if (getMessage[0] == MessageTrackerId) {
                    setFieldError('TrackerId', 'Tracker ID is Already Assigned')
                }

                if (getMessage[0] == MessagePlateNumber) {
                    setFieldError('fleetPlateNumber', 'Plate Number Alreafy assigned')
                }

            })
       
        return {       
            sendCreateVehicle,
            fleetPlateNumber,
            TrackerId,
            TrackerPhoneNum,
            category,
            vechileName,
            createFleet,
            onSubmit,

            showSuccess,
            sendMessageLoading,           
            //errors
            sendMessageError,
            TrackerIdError,
            categoryError,
            vechileNameError,
            fleetPlateNumberError,
            TrackerPhoneNumError
        }        
    }
    
}
</script>


<style scoped>
.mode {
    margin: auto;
    background-color: rgb(255, 255, 255);
    padding: 30px;
    
    height: 380px;
    overflow: scroll;   
    border-radius: 20px; 
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
    width: max-content;
    top: 100px;
    right: 0;
    z-index: 1;
}

.submitError{
    background: rgb(255, 184, 184);
    border-radius: 20px;
    padding: 20px;
    width: max-content;
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