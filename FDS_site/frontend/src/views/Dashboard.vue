<template> 
 <main role="main">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-2 dashboard-body">
                    <section class="text-left links">
                        <router-link :to="{name: 'Summary'}">
                            <div class="d-flex flex-row bd-highlight mb-3 background">
                                <div class="p-2 bd-highlight">
                                <h6><i class="fas fa-home"></i> </h6>
                                </div>                                  
                                <div class="p-2 bd-highlight">
                                <h6 role="button">Dashboard</h6>
                                </div>                            
                            </div>
                        </router-link>
                        
                        <router-link :to="{ name: 'Customers' }"> 
                            <div class="d-flex flex-row bd-highlight mb-3 background">
                                <div class="p-2 bd-highlight">
                                <h6>
                                    <i class="fas fa-truck"></i>
                                    </h6>
                                </div>
                                <div class="p-2 bd-highlight">
                                    <h6 role="button">Customers</h6>
                                </div>                            
                            </div>
                        </router-link>

                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                   <i class="fas fa-users"></i>
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <a href=""><h6 role="button">Riders</h6></a>
                            </div>                            
                        </div>

                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-file-invoice-dollar"></i> 
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <a href=""><h6 role="button">Front Desk</h6></a>
                            </div>                            
                        </div>
                                                
                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-comment-alt"></i>                                
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <h6 role="button">Orders</h6>
                            </div>                            
                        </div>         

                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-comment-alt"></i>                                
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <h6 role="button">Send SMS</h6>
                            </div>                            
                        </div>     

                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-comment-alt"></i>                                
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <h6 role="button">Buy Airtime</h6>
                            </div>                            
                        </div> 

                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-comment-alt"></i>                                
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <h6 role="button">Tracking Website</h6>
                            </div>                            
                        </div> 

                        <div class="d-flex flex-row bd-highlight mb-3 background">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-comment-alt"></i>                                
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <h6 role="button">Markerting</h6>
                            </div>                            
                        </div> 

                        <div class="d-flex flex-row bd-highlight mb-3 background text-center">
                            <div class="p-2 bd-highlight">
                               <h6>
                                    <i class="fas fa-comment-alt"></i>                                
                                </h6>
                            </div>
                            <div class="p-2 bd-highlight">
                                <h6 role="button">Report</h6>
                            </div>                            
                        </div>

                    </section>
                </div>
                <div class="col-md-10">
                    <section class="top p-3">
                        <a href="" role="button" class="btn btn-primary btn-sm">
                            Notifications <span class="badge badge-light">0</span>
                        </a>
                    </section>
                    <div class="the-body mt-3">
                        <div class="container">
                            <div class="row">
                                <div class="col"></div>
                                <div class="col">
                                    <router-view/>                                 
                                </div>
                                <div class="col"></div>
                            </div>    
                        </div>
                        
                      
                    </div>   
                </div>
            </div> 
        </div>
    </main>  
</template>


<style scoped>
    * {
  box-sizing: border-box;
    }
    .dashboard-body{
            background-color: rgb(16, 0, 61);        
            height: 620px;
            overflow: auto;
        }

    .links{
        margin-top: 50px;
        color: white;
    }
    
    h6{        
        font-family: 'Nunito', sans-serif;
        font-weight: 700;
        font-size: 15px;
    }

    h6:hover{
        background-color: rgb(235, 240, 255);
        color: rgb(1, 20, 88);
        font-family: 'Nunito', sans-serif;
        font-weight: 700;
        font-size: 15px;              
    }

    .background:hover{
        background-color: rgba(239, 243, 255, 1);
        color: rgba(0, 29, 130, 1);
        width: auto; 
        border-radius: 20px;          
    }    

    .top{
        background-color: white;
        box-shadow:  0px 4px 4px rgba(65, 9, 9, 0.08);
        width: auto;
        height: autox;                
    }

    .the-body{
        height: 530px;
        overflow: scroll;
    }    

    /*Working on the scroll bar*/
    ::-webkit-scrollbar{
        width: 7px;
    }

    ::-webkit-scrollbar-track {
        border-radius: 50px;
    }

    ::-webkit-scrollbar-thumb {
        background-color: rgb(233, 240, 255);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: rgb(182, 215, 255);
    }
  </style>

