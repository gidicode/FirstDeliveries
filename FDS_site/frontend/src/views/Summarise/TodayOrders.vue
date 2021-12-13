<template>
    <div class="backdrop" >
        <div class="row" >        
            <div class="col-md-2" @click.self= "sendEvent"></div>
                <div class="col-md-8" @click.self= "sendEvent">
                    <main class="mode">                    
                        <h5>Deliveries Today</h5>        
                        <small class="explain">Orders of different category 
                            (Delivered, canceled, Pending)
                            from all service point.
                        </small>                    
                        <hr>
                        <div class="accordion accordion-flush" id="accordionFlushExample">
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="flush-headingOne">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                                    <div class="d-flex flex-row bd-highlight">
                                        <div class="bd-highlight widths">Customers Orders</div>
                                        <div class="bd-highlight"> <span class="badge alert-primary ms-2 w-80">{{ cashLength }}</span></div>                                    
                                    </div>                                 
                                </button>
                                </h2>
                                <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
                                <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.</div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="flush-headingTwo">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                                    <div class="d-flex flex-row bd-highlight">
                                        <div class="bd-highlight widths"> Errand Orders</div>
                                        <div class="bd-highlight"> <span class="badge alert-primary ms-2 w-80">{{ errandLength }}</span></div>
                                    </div>                               
                                </button>
                                </h2>
                                <div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionFlushExample">
                                <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the second item's accordion body. Let's imagine this being filled with some actual content.</div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="flush-headingThree">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                                    <div class="d-flex flex-row bd-highlight">
                                        <div class="bd-highlight widths">  Front Desk Orders </div>
                                        <div class="bd-highlight"> <span class="badge alert-primary ms-2 w-80">{{ frontLength }}</span></div>                                    
                                    </div>                                  
                                </button>
                                </h2>
                                <div id="flush-collapseThree" class="accordion-collapse collapse" aria-labelledby="flush-headingThree" data-bs-parent="#accordionFlushExample">
                                <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.</div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="flush-headingFour">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseFour" aria-expanded="false" aria-controls="flush-collapseFour">
                                    <div class="d-flex flex-row bd-highlight justify-content-between">
                                        <div class="bd-highlight widths"> Shopping Orders</div>                                    
                                        <div class="bd-highlight"> <span class="badge alert-primary ms-2 w-80">{{ shoppingLength }}</span></div>                                                                        
                                    </div>                                 
                                </button>
                                </h2>
                                <div id="flush-collapseFour" class="accordion-collapse collapse" aria-labelledby="flush-headingFour" data-bs-parent="#accordionFlushExample">
                                <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.</div>
                                </div>
                            </div>
                        </div>
                    </main>
                </div>
            <div class="col-md-2" @click.self= "sendEvent"></div>       
        </div>
    </div>
</template>


<script>
export default {
    name:"OrdersToday",
    props: {cashLength:Number,
            errandLength:Number,
            frontLength:Number,
            shoppingLength:Number,            
    },
    emits: ['close'],
    
    setup(props, context){
        const sendEvent = () => {                  
            context.emit('close') 
        }
    return { sendEvent}
    }    
}
</script>

<style scoped>
.mode {
    margin: 100px auto;
    background-color: rgb(255, 255, 255);    
    padding: 20px;    
    height: 380px;
    overflow: scroll; 
}

.backdrop{
    top: 70px;
    position: fixed;
    background: rgba(0, 0, 0, 0.5);
    width: 75%;
    height: auto;
    border-radius: 20px;
}

.explain{
    position: relative;
    top: -9px;
    color: rgb(6, 0, 61);    
}

h5 {
    color: rgb(6, 0, 61);
}

.widths {
    width: 130px;
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