<template>
    <div>
        <div class="close-text" @click="sendCloseEvent">
            <small>
                <i class="fas fa-times"></i>
            </small>
        </div>
        <div class="picture">
            <i class="far fa-user-circle text-primary "></i>
        </div>        

        <table class="table">
          
            <tbody class="text-white">
                <tr>            
                <td class="fw-bold">First Name</td>
                <td>{{firstName}}</td>                
                </tr>
                <tr>                
                <td class="fw-bold">Last Name</td>
                <td>{{ lastName }}</td>                
                </tr>
                <tr>                
                <td class="fw-bold">Email Address</td>
                <td>{{ email}}</td>                
                </tr>                
                 <tr>                
                <td class="fw-bold">Username</td>
                <td>{{ username }}</td>                
                </tr>   
                 <tr>                
                <td class="fw-bold">1st Contact</td>
                <td>{{ phoneNumber }}</td>                
                </tr>   
                <tr>                
                <td class="fw-bold">2nd Contact</td>
                <td>{{ altPhoneNum }}</td>                
                </tr>  
                <tr>                
                <td class="fw-bold">Date Registered</td>
                <td>{{ dateJoined }}</td>                
                </tr>  
            </tbody>
            </table>      
        
    </div>   
</template>


<script>
import { computed } from '@vue/runtime-core'
import { useRoute } from 'vue-router'


export default {
    name:"CustomersDetails",
    emits: ['closeDetails'],

    setup(props, context) {        
        const route = useRoute()
        const firstName = computed(() => route.params.firstName)
        const lastName = computed(() => route.params.lastName)
        const email = computed(() => route.params.email)
        const username = computed(() => route.params.username)
        const phoneNumber = computed(() => route.params.phoneNumber)
        const altPhoneNum = computed(() => route.params.altPhoneNum)
        const dateJoined = computed(() => route.params.dateJoined)                
        const sendCloseEvent = () => {                  
            context.emit('closeDetails') 
        }        
        return {
            firstName,
            lastName,
            email,
            username,
            phoneNumber,
            altPhoneNum,
            dateJoined,  
            sendCloseEvent                           
        }
    }
}
</script>

<style scoped>
.picture {
    font-size: 100px;
    margin: auto;
    text-align: center;
}

h6 {
    font-family: 'Nunito', sans-serif;
}

.close-text {
    text-align: right;
    margin: auto;
       
    right: auto;
}

.close-text small {
    cursor: pointer; 
    color: rgb(106, 165, 255);
}
</style>