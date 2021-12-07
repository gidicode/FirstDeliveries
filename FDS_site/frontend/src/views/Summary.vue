<template >
    <div class="container mt-1" id="summ1" >
        <div class="row no-gutters">
            <div class="col">            
                <div class="d-flex flex-row bd-highlight mb-3 justify-content-right">
                    <div class="p-2 bd-highlight">
                        <section class="affiliate-customers">
                            <h5 class="all-affiliate-customers">Total <br>Customers</h5>
                            <div class="affiliate-marketer-count-background text-center">
                                <h3 class="affiliate-marketer-count">{{ count_customers }}</h3>
                            </div>
                            <figure class="customers_icon_background">
                                <i class="fas fa-users customers_icon"></i>                            
                            </figure>
                        </section>
                    </div>

                    <div class="p-2 bd-highlight">
                        <section class="Total_deliveries" >                            
                            <h5 class="Total_deliveries_font">Total <br>Deliveries</h5>
                            <div class="Total_deliveries_count_background text-center">
                                <h3 class="Total_deliveries_count"> {{ count_Delivery.length }}</h3>
                            </div>
                            <figure class="Total_deliveries_icon_background text-center">
                                <i class="far fa-clock Total_deliveries_icon"></i>
                            </figure>
                        </section>
                    </div>  
                    

                    <div class="p-2 bd-highlight">
                        <section class="Pending_deliveries_section">
                            <h5 class="Pending_deliveries">Total <br> Riders</h5>
                            <div class="Pending_deliveries_count_background">
                                <h3 class="Pending_deliveries_count">{{ count_riders }}</h3>
                            </div>
                            <figure class="Pending_deliveries_icon_background text-center">                                                        
                                <i class="fas fa-hourglass-half Pending_deliveries_icon"></i>
                            </figure>
                        </section>
                    </div>


                    <div class="p-2 bd-highlight">
                        <section class="Pending_payout_section">
                            <h5 class="Pending_payout">Pending <br> Deliveries</h5>                        
                            <div class="Pending_payout_count_background">
                                <h3 class="Pending_payout_count">{{ count_pending }}</h3>
                            </div>
                            <figure class="Pending_payout_icon_background text-center"> 
                                <i class="fas fa-money-bill Pending_payout_icon"></i>                                                                                   
                            </figure>                       
                        </section>
                    </div> 
                </div>
            </div>


            <div class="col">            
                <div class="d-flex flex-row bd-highlight mb-3 justify-content-right">
                    <div class="p-2 bd-highlight">
                        <section class="Total_delivery_fee_section">
                            <h5 class="Total_delivery_fee">Total <br>Fleet</h5>
                            <div class="Total_delivery_fee_calculation_background text-center">
                                <h3 class="Total_delivery_fee_calculation">{{ count_fleet }}</h3>
                            </div>
                            <figure class="Total_delivery_fee_icon_background">
                                <i class="fas fa-truck Total_delivery_fee_icon"></i>
                            </figure>
                        </section>
                    </div>

                    <div class="p-2 bd-highlight">
                        <section class="Credited_marketers_section">
                            <h5 class="Credited_marketers">FrontDesk<br>Requests</h5>
                            <div class="Credited_marketers_sum_background text-center">
                                <h3 class="Credited_marketers_sum">{{ count_frontdesk }}</h3>
                            </div>
                            <figure class="Credited_marketers_icon_background text-center">
                                <i class="fas fa-money-bill Credited_marketers_icon"></i>                            
                            </figure>
                        </section>
                    </div>                      

                    <div class="p-2 bd-highlight">
                        <section class="Total_cashout_section">
                            <h5 class="Total_cashout">Customers<br>Contact</h5>
                            <div class="Total_cashout_sum_background"> 
                                <h3 class="Total_cashout_sum">{{ count_contacts }}</h3>
                            </div>
                            <figure class="Total_cashout_icon_background text-center">                             
                                <i class="fas fa-money-bill Total_cashout_icon"></i>                                                                                   
                            </figure>
                        </section>
                    </div>

                    <div class="p-2 bd-highlight">
                        <section class="Balance_marketers_section">
                            <h5 class="Balance_marketers">Balance <br> To Marketers</h5>                        
                            <div class="Balance_marketers_sum_background">
                                <h3 class="Balance_marketers_sum">N</h3>
                            </div>
                            <figure class="Balance_marketers_icon_background text-center">
                                <i class="fas fa-money-bill-wave-alt Balance_marketers_icon"></i>                            
                            </figure>
                        </section>
                    </div> 
                </div>
            </div>                          
        </div>                    
    </div>    
</template>

<script>
export default {
    data() {
        return {
          count_Delivery: [
              {id:1, details:"wow"},
              {id:2, details:"thats good"},
              {id:3, details:"intresting"}
          ],          
          count_customers: 50,
          count_riders: 40,
          count_pending: 20,
          count_fleet: 20,
          count_frontdesk: 322,
          count_contacts: 56,        
        }
    },
    created() {
        this.count_Delivery.length
    },
}
</script>

<style scope>  
    .affiliate-customers{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .all-affiliate-customers{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }    
    .affiliate-marketer-count-background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .affiliate-marketer-count{       
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;                     
    }
    .customers_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .customers_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }
    

    .Total_deliveries{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Total_deliveries_font{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }    
    .Total_deliveries_count_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Total_deliveries_count{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Total_deliveries_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Total_deliveries_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }


    .Pending_deliveries_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Pending_deliveries{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Pending_deliveries_count_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Pending_deliveries_count{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Pending_deliveries_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Pending_deliveries_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }

    .Pending_payout_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Pending_payout{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Pending_payout_count_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Pending_payout_count{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Pending_payout_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Pending_payout_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }

    .Total_delivery_fee_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Total_delivery_fee{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Total_delivery_fee_calculation_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Total_delivery_fee_calculation{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Total_delivery_fee_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Total_delivery_fee_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }

    .Credited_marketers_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Credited_marketers{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Credited_marketers_sum_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Credited_marketers_sum{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Credited_marketers_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Credited_marketers_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }

    .Total_cashout_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Total_cashout{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Total_cashout_sum_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Total_cashout_sum{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Total_cashout_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Total_cashout_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }

    .Balance_marketers_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Balance_marketers{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Balance_marketers_sum_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Balance_marketers_sum{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Balance_marketers_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Balance_marketers_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }


    .Total_profit_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Total_profit{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Total_profit_calculation_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Total_profit_calculation{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Total_profit_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Total_profit_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }


    .Total_today_section{
        width: 232px;
        height: 131px;                
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;        
        position: relative;
    }
    .Total_today{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .Total_today_sum_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Total_today_sum{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Total_today_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Total_today_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }


    .Deliveries_today_section{
        width: 232px;
        height: 131px;
        background: rgba(255, 255, 255, 1);
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 10px;
        position: relative;
    }
    .Deliveries_today{
        position: relative;
        top: 10px;
        left: 10px;
        color: rgba(83, 1, 1, 1);
        font-family: 'Nunito', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }
    .TDeliveries_today_count_background{
        padding: 2px;   
        background-color: rgba(255, 235, 235, 1);
        width: max-content;
        border-radius: 5px; 
        margin-top: 48px;
        margin-left: 18px;
    }
    .Deliveries_today_count{
        top: 50px;        
        color: rgba(83, 1, 1, 1);
        font-family: 'Roboto', sans-serif; 
        font-size: 20px;
        font-weight: 800;    
    }
    .Deliveries_today_icon_background{
        padding: 5px 8px;
        border-radius: 50%;               
        width: 52px;
        height: 52px;
        background: rgba(255, 235, 235, 1);
        backdrop-filter: blur(10px);       
        margin-top: -80px;
        margin-left: 170px;
    }
    .Deliveries_today_icon{
        color: rgba(83, 1, 1, 1);
        position: relative;
        right: -3px;
        top: 20%;
        font-size: 25px;
    }       
</style>

{% endblock content %}