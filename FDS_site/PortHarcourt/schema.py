from django.contrib.auth import get_user_model
from graphene.types import schema

from graphene_django import DjangoObjectType
import graphene

from PortHarcourt import models
from users import models as Usersmodels

from datetime import datetime

today = datetime.now().date()   

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CustomerType(DjangoObjectType):
    class Meta:
        model = Usersmodels.Customer

class FleetType(DjangoObjectType):
    class Meta:
        model = models.Fleets_PH

class RidersType(DjangoObjectType):
    class Meta:
        model = models.RidersProfile_PH

class CashType(DjangoObjectType):
    class Meta:
        model = models.MakeRequestCash_PH

class ErrandType(DjangoObjectType):
    class Meta:
        model = models.Errand_service_PH

class Front_DeskType(DjangoObjectType):
    class Meta:
        model = models.Front_desk_PH

class ShoppingType(DjangoObjectType):
    class Meta:
        model = models.Shopping_PH

class AdminType(DjangoObjectType):
    class Meta:
        model = models.PH_adminNotification

class ContacType(DjangoObjectType):
    class Meta:
        model = models.Contact_of_customers


class Query(graphene.ObjectType):
    #riders & Fleet
    all_fleets = graphene.List(FleetType) 
    def resolve_all_fleets(root, info):
        return models.Fleets_PH.objects.all()

    all_riders = graphene.List(RidersType)
    def resolve_all_riders(root, info):
        return models.RidersProfile_PH.objects.all()

    #allRecords
    all_cash_requests = graphene.List(CashType)
    def resolve_all_cash_requests(root, info):
        return models.MakeRequestCash_PH.objects.all()

    all_errand_service = graphene.List(ErrandType)
    def resolve_all_errand_service(root, info):
        return models.Errand_service_PH.objects.all()

    all_front_desk = graphene.List(Front_DeskType)
    def resolve_all_front_desk(root, info):
        return models.Front_desk_PH.objects.all()

    all_shopping = graphene.List(ShoppingType)
    def resolve_all_shopping(root, info):
        return models.Shopping_PH.objects.all()
   
    all_admin = graphene.List(AdminType)
    def resolve_all_admin(root, info):
        return models.PH_adminNotification.objects.all()

    #Filter By delivered
    byCashDelivered = graphene.List(CashType)
    def resolve_byCashDelivered(root, info):
        return models.MakeRequestCash_PH.objects.filter(status = 'Delivered')

    byErrandDelivered = graphene.List(ErrandType)
    def resolve_byErrandDelivered(root, info):
        return models.Errand_service_PH.objects.filter(status = 'Delivered')

    byFrontDeskDelivered = graphene.List(Front_DeskType)
    def resolve_byFrontDeskDelivered(root, info):
        return models.Front_desk_PH.objects.filter(status = 'Delivered')

    byAllShoppingDelivered = graphene.List(ShoppingType)
    def resolve_byAllShoppingDelivered(root, info):
        return models.Shopping_PH.objects.filter(status = 'Delivered') 

    #Filter By pending
    byCashPending = graphene.List(CashType)
    def resolve_byCashPending(root, info):
        return models.MakeRequestCash_PH.objects.filter(status = 'Pending')

    byErrandPending = graphene.List(ErrandType)
    def resolve_byErrandPending(root, info):
        return models.Errand_service_PH.objects.filter(status = 'Pending')

    byFrontDeskPending = graphene.List(Front_DeskType)
    def resolve_byFrontDeskPending(root, info):
        return models.Front_desk_PH.objects.filter(status = 'Pending')

    byAllShoppingPending = graphene.List(ShoppingType)
    def resolve_byAllShoppingPending(root, info):
        return models.Shopping_PH.objects.filter(status = 'Pending') 

    #customers
    allCustomers = graphene.List(CustomerType)
    def resolve_allCustomers(root, info):
        return Usersmodels.Customer.objects.filter(Location = 'Port Harcourt') 

    #contact
    allContact = graphene.List(ContacType)
    def resolve_allContact(root, info):
        return models.Contact_of_customers.objects.all()

    #Filter By Date
    byCashDate = graphene.List(CashType)
    def resolve_byCashDate(root, info):        
        return models.MakeRequestCash_PH.objects.filter(date_created__date =today)
    byErrandDate = graphene.List(ErrandType)
    def resolve_byErrandDate(root, info):
        return models.Errand_service_PH.objects.filter(date_created__date =today)

    byFrontDeskDate = graphene.List(Front_DeskType)
    def resolve_byFrontDeskDate(root, info):
        return models.Front_desk_PH.objects.filter(date_created__date =today)

    byAllShoppingDate = graphene.List(ShoppingType)
    def resolve_byAllShoppingDate(root, info):
        return models.Shopping_PH.objects.filter(date_created__date =today)


#**********************************MUTATION*************************#
class CreateRiders(graphene.Mutation):    
    class Arguments:
        id = graphene.ID()
        attached_bike_id = graphene.Int(name="attachedBike")
        first_name = graphene.String()
        last_name = graphene.String()
        phone_number = graphene.String()        
        Address = graphene.String()                    
    riders = graphene.Field(RidersType)
    
    @classmethod
    def mutate(
            root, info, id, attached_bike_id, first_name, 
            last_name, phone_number, Address
        ):        
        riders = models.RidersProfile_PH.objects.create(
            first_name = first_name, 
            last_name = last_name,
            phone_number = phone_number,             
            Address = Address,
        ) 
        if attached_bike_id is not None:           
            attached_bike_object = models.Fleets_PH.objects.get(pk = attached_bike_id)                        
        riders.attached_bike = attached_bike_object
        riders.save()        
        return CreateRiders(riders=riders)

class CreateFleet(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        fleet_plate_number = graphene.String()
        Tracker_id = graphene.String()
        Tracker_phone_num = graphene.String()
        category = graphene.String()
        vehicle_name = graphene.String()
        date_created = graphene.types.DateTime()

    fleet = graphene.Field(FleetType)

    @classmethod
    def mutate( 
        root, info, id, fleet_plate_number, 
        Tracker_id, Tracker_phone_num, category,
        vehicle_name, date_created
    ):
        fleet = models.Fleets_PH.objects.create(
            fleet_plate_number = fleet_plate_number,
            Tracker_id = Tracker_id, Tracker_phone_num = Tracker_phone_num,
            category = category, vehicle_name = vehicle_name, 
            date_created = date_created
        )
        return CreateFleet(fleet = fleet)
        
class Mutation(graphene.ObjectType):
    createRiders = CreateRiders.Field()
    createFleet = CreateFleet.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)