<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col">      
                <div class="riders-list shadow mb-4">
                    <p>You currently doo not have riders registered</p>
                    <button class="btn btn-sm addBtn rounded" @click="changeRiderFormState"><i class="fas fa-user-plus"></i> Add Rider</button>
                </div>   

                <div class="riders-list shadow mb-4">
                    <p>You currently doo not have Vehicles registered</p>
                    <button class="btn btn-sm addBtn rounded"><i class="fas fa-user-plus"></i> Add Vehicles</button>
                </div>   

                <div class="d-flex flex-row bd-highlight justify-content-around mb-3">
                    <div class="p-2 bd-highlight">                                  
                        <button class="btn btn-sm viewBtn rounded-pill ">
                            <i class="fas fa-eye"></i>
                             Riders
                        </button>
                       
                    </div>
                    <div class="p-2 bd-highlight">                                       
                        <button class="btn btn-sm viewBtn rounded-pill ">
                            <i class="fas fa-eye"></i>
                            Vehicles
                        </button>                        
                    </div>                    
                </div>                            
            </div>
            <div class="col">
                <div v-if="ViewRiderForm">
                    <AddRiderForm @CloseRidersForm="changeRiderFormState"/>
                </div>
            </div>
            <div class="col">
            Column
            </div>
        </div>
    </div>
</template>

<script>
import AddRiderForm from './AddRiderForm.vue'
import { ref } from '@vue/reactivity'

export default {
    name:'RidersPage',
    components: {AddRiderForm},

    setup() {
        const ViewRiderForm = ref(false)
        const changeRiderFormState = () => ViewRiderForm.value = !ViewRiderForm.value
        return {
            AddRiderForm,
            ViewRiderForm,
            changeRiderFormState
        }
    }
    
}
</script>

<style scoped>
.riders-list {
  text-align: left;
  color: rgb(0, 8, 43);
  background: rgb(255, 251, 251);  
  width: max-content;
  padding: 20px;
  border-radius: 10px;
}

.addBtn {
    background: rgb(17, 33, 70);
    color: rgb(255, 255, 255);
    font-weight: bold;
    
}
.addBtn:hover{
    background: rgb(31, 64, 143);
    color: rgb(255, 255, 255);
    font-weight: bold;
    box-shadow: 5px 7px 14px #c2c2c2;
}

.viewBtn{
    background: rgb(0, 110, 184);
    color: rgb(255, 255, 255);
    font-weight: bold;
    padding: 8px;
    width: 150px;
}

.viewBtn:hover{
    background: rgb(31, 64, 143);
    color: rgb(255, 255, 255);
    font-weight: bold;
    box-shadow: 5px 7px 14px #c2c2c2;
}

</style>