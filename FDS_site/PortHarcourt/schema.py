from django.contrib.auth import get_user_model
from graphene.types import schema

from graphene_django import DjangoObjectType
import graphene

from PortHarcourt import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

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


class Query(graphene.ObjectType):
    all_fleets = graphene.List(FleetType) 
    all_riders = graphene.List(RidersType)
    all_cash_requests = graphene.List(CashType)
    all_errand_service = graphene.List(ErrandType)
    all_front_desk = graphene.List(Front_DeskType)
    all_shopping = graphene.List(ShoppingType)
    all_admin = graphene.List(AdminType)

    def resolve_all_fields(root, info):
        return models.Fleets_PH.objects.all()

    def resolve_all_riders(root, info):
        return models.RidersProfile_PH.objects.all()

    def resolve_all_cash_requests(root, info):
        return models.MakeRequestCash_PH.objects.all()

    def resolve_all_errand_service(root, info):
        return models.Errand_service_PH.objects.all()

    def resolve_all_front_desk(root, info):
        return models.Front_desk_PH.objects.all()

    def resolve_all_shopping(root, info):
        return models.Shopping_PH.objects.all()

    def resolve_all_admin(root, info):
        return models.PH_adminNotification.objects.all()

schema = graphene.Schema(query=Query)