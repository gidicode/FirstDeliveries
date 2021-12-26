<template>
    <div class="backdrop">
        <p class="close-text" @click="sendCreateVehicle">
            <i class="fas fa-times"></i>
        </p>
        <div class="row" >        
            <div class="col-md-2" ></div>
                <div class="col-md-8" >                   
                    <main class="mode container-lg">                          
                        <form class="row g-3" @submit.prevent="createFleet()">
                            <div class="col-md-6">
                                <label for="plateNumber" class="form-label">Plate Number</label>
                                <input type="text" class="form-control" required id="plateNumber" v-model="fleetPlateNumber">
                            </div>
                            <div class="col-md-6">
                                <label for="trackerId" class="form-label">Tracker Id</label>
                                <input type="text" class="form-control" required id="trackerId" v-model="TrackerId">
                            </div>
                            <div class="col-md-6">
                                <label for="trackerPhoneNumber" class="form-label">Tracker Phone Number</label>
                                <input type="text" class="form-control" required id="trackerPhoneNumber" v-model="TrackerPhoneNum" placeholder="Contact inside tracker">
                            </div>                           
                            
                            <div class="col-md-6">
                                <label for="vechileName" class="form-label">Vehicle Name</label>
                                <input type="text" class="form-control" required id="vechileName" v-model="vechileName" placeholder="Brief Description of vehicle">
                            </div>  
                                                                                     
                            <div class="col-12">
                                <label for="category" class="form-label">Category </label>
                                <select id="category" class="form-select" required v-model="category">
                                    <option selected>Choose...</option>
                                     <option >Bike</option>
                                     <option >Tricycle</option>
                                     
                                </select>
                            </div>                  

                            <div class="col-12"> 
                                <button type="submit" class="btn btn-primary" >Submit</button>
                            </div>
                        </form>                                                                                             
                    </main>
                </div>
            <div class="col-md-2" >
                <div v-if="sendMessageError" class="errorBackground">
                    <p>An error Occured</p>
                </div>
            </div>
        </div>
    </div> 
</template>


<script>
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'
import { ref } from '@vue/reactivity'

export default {
    name:"AddVehicles",
    emits: ['CloseVehicleForm'],

    setup(props, context){
        const sendCreateVehicle = () => {
            context.emit('CloseVehicleForm')
        } 
        const fleetPlateNumber = ref('')
        const TrackerId = ref('')
        const TrackerPhoneNum = ref('')
        const category = ref('')
        const vechileName = ref('')

        const {mutate: createFleet, error: sendMessageError, } = useMutation(gql`
            mutation createFleet(
                $fleetPlateNumber: String!,
                $TrackerId: String!,
                $TrackerPhoneNum: String!,
                $category: String!,
                $vechileName:String!
                $dateCreated: DateTime! 
                )
                {
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

       
        return {       
            sendCreateVehicle,
            fleetPlateNumber,
            TrackerId,
            TrackerPhoneNum,
            category,
            vechileName,
            createFleet,
            sendMessageError
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

.errorBackground{
    background: antiquewhite;
    padding: 20px;
    border-radius: 10px;
    width: auto;
    height: min-content;
    position: absolute;
    z-index: 1;
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