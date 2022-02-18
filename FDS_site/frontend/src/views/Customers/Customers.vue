<template>
    <div class="row">
      <div class="col-md-4">
        <section class="details-background shadow-sm ">                          

          <div class="d-flex flex-row bd-highlight mb-3 td-data"
           v-for=" i in allCustomers" :key="i.id"
           >
            <router-link :to="{name: 'CustomerDetails', 
              params: {
                id: i.id,
                firstName: i.firstName,
                lastName: i.lastName,
                email: i.email,
                username: i.user.username,
                phoneNumber: i.phoneNumber,
                SecondNumber: i.AltPhoneNum,
                dateJoined: i.user.dateJoined
                }}"
            >
              <div class="p-1 bd-highlight" @click="changeStateOnce"> 
                <span class="p-2"><i class="far fa-user-circle "></i></span> 
                <span class="p-2">{{ i.firstName }} {{ i.lastName }} </span>
                <span class="p-2"> {{i.phoneNumber}} </span>
              </div>                             
            </router-link>
          </div>          
        </section>
      </div>

      <div class="col-md-2"></div>

      <div class="col-md-6"> 
        <div v-if="showPage" class="customerDetailsBackground">
          
          <CustomerDetails @closeDetails="changeState" />  
        </div>        
      </div>
    </div> 

</template>


<script>
import { computed, ref } from '@vue/reactivity'
import {allPHcustomers} from '../../graphql'
import CustomerDetails from './CustomerDetails.vue'

export default {  
  name: "Customers",
  components: {CustomerDetails},
  setup() {
    const allCustomers = computed(() => allPHcustomers.value) 
    const showPage = ref(false)
    const changeState = () => showPage.value = !showPage.value
    const changeStateOnce = () => showPage.value = true    
    
    return {
      allCustomers,      
      showPage,
      changeStateOnce,    
      changeState,
      CustomerDetails     
    }
  }
}
</script>


<style scoped>  
.customerDetails {
  text-align: left;
  color: rgb(255, 255, 255);
  background: rgb(135, 187, 255);  
  width: max-content;
  padding: 4px;
  border-radius: 10px;
}

.details-background {
  background: rgb(245, 245, 255);
  padding: 20px;
  border-radius: 20px;  
  overflow: scroll;
  height: 500px;
}

.details-background a.router-link-exact-active {
   background-color: rgb(243, 243, 243);
  color: rgb(150, 151, 184);
  border-radius: 20px;
  font-weight: bold;
  cursor: context-menu;
  box-shadow: 5px 10px 18px #c2c2c2;
  text-align: center;
}

.title-background{
  background: rgb(122, 164, 255);
  color: rgb(253, 185, 185);
  padding: 5px;  
}

.td-data:hover{
  background-color: rgb(243, 243, 243);
  color: rgb(150, 151, 184);
  border-radius: 20px;
  font-weight: bold;
  cursor: context-menu;
  box-shadow: 5px 10px 18px #c2c2c2;
  text-align: center;
}

.td-data a {
  text-decoration: none;  
}

.customerDetailsBackground {
  background: rgb(0, 57, 143);
  box-shadow: 5px 10px 15px rgb(163, 163, 163);
  padding: 20px;
  border-radius: 10px;
  color: white;
}

.details-background::-webkit-scrollbar{
        width: 7px;
}

.details-background::-webkit-scrollbar-track {
    border-radius: 50px;
}

.details-background::-webkit-scrollbar-thumb {
    background-color: rgb(56, 110, 228);
    border-radius: 5px;
}

.details-background::-webkit-scrollbar-thumb:hover {
    background-color: rgb(9, 38, 73);
}
</style>

{% endblock content %}