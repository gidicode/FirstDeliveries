from users.forms import Shopping_Form
from django import forms
from django.core.exceptions import ValidationError
from.models import MakeRequestCash_PH,  Errand_service_PH, Front_desk_PH, Shopping_PH
from users.models import Anonymous
class Request_Cash_PH(forms.ModelForm):
    OPTIONS2 = [
            #( "Van", "Van"),
            ("Bike", "Bike"),
            #( "Tricycle", "Tricycle (Keke)"),
    ]
    #LOADING_CHOICE = [
            #("loading", "Loading"),
            #( "off Loading", "Off Loading"),
    #]
    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect)
    reciever_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=True, label='Reciever Number',
                    min_length=11, widget= forms.TextInput)
    reciever_name2 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (2)'}))
    reciever_name3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (3)'}))
    reciever_name4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (4)'}))
    reciever_name5 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (5)'}))
    Address_of_reciever3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (3)'}))
    Address_of_reciever3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (3)'}))
    Address_of_reciever4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Addressof reciever (4)'}))
    Address_of_reciever5 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (5)'}))                                                      
    Package_description2 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (2)'}))   
    Package_description3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (3)'}))   
    Package_description4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (4)'}))   
    Package_description5 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Packagen description (5)'}))    

    reciever_phone_number2 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number (2)'}))
    reciever_phone_number3 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number(3)'}))
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11,  widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number(4)'}))
    reciever_phone_number5 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number(5)'}))    
    class Meta:
        model = MakeRequestCash_PH
        fields = '__all__'
        exclude = ['type', 'Amount_Paid', 'customer', 'date_created', 'status', 'paid',  'order_id', 'assigned', 'Amount_Payable', 'Loading_choice' ]

class Fuel_errand_PH(forms.ModelForm):
    class Meta:
        model =  Errand_service_PH
        fields = ['fuel_per_amount', 'payment_channel', 'your_location']

class Gas_errand_PH(forms.ModelForm):

    class Meta:
        model =  Errand_service_PH
        fields = ['Gas_Quantity', 'payment_channel', 'your_location']

def chk_drug(value):
    illegal_drugs = [
                    'Codeine', 'codeine', 'CODEINE', 'Codine', 
                    'codine', 'Codin', 'codin', 'Rohypnol', 'rohypnol', 
                    'refnol', 'Rohynol', 'rohynol', 'GHB', 'ghb', 'Ghb', 
                    'Ketamine', 'ketamine', 'methamphetamine', ' heroin', 'diazepam', 
                    'cough syrup', 'tramadol', 'Tramadol', 'TRAMADOL', 'MDMA', 
                    'ectasy', 'Ectasy' 'Lysergic acid diethylamide'
                    'LSD', 'Valium', 'morphine', 'Fentanyl', 'Ritalin', 
                    'ritalin', 'RITALIN', 'Oxymorphon', 'oxymorphon', 'Adderal'
                    ]
    if value in illegal_drugs:
        raise ValidationError((f'{value} falls under the drug abuse category and we cant purchase it.'), params= {'value':value})

class Drugs_errand_PH(forms.ModelForm):
    Drug_name = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter list of specified drugs", 'row':3}), validators= [chk_drug],  )
    class Meta:

        model =  Errand_service_PH
        fields = ['Drug_store', 'Drug_store_location', 'Drug_name', 'medical_prescription', 'Enter_amount', 'payment_channel', 'your_location']

class Bread_errand_PH(forms.ModelForm):
    class Meta:

        model =  Errand_service_PH
        fields = ['Bread_brand_name', 'Quantity', 'description', 'Enter_amount', 'payment_channel', 'your_location']

class Shawarma_errand_PH(forms.ModelForm):
    class Meta:

        model =  Errand_service_PH
        fields = ['Shawarma_store', 'Shawarma_desc', 'description', 'Quantity',  'Enter_amount', 'payment_channel', 'your_location']

class Pizza_errand(forms.ModelForm):
    class Meta:

        model =  Errand_service_PH
        fields = ['pizza_store', 'Pizza_desc', 'description', 'Quantity',  'Enter_amount', 'payment_channel', 'your_location']

class Fruits_errand(forms.ModelForm):
    class Meta:
        fruits_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Name of fruit and the quantity", 'row':2}))
        model =  Errand_service_PH
        fields = [ 'fruits_purchase_store', 'fruits_description', 'Enter_amount', 'payment_channel', 'your_location']

class Icecream_errand(forms.ModelForm):
    class Meta:
        model =  Errand_service_PH
        fields = [ 'ice_Cream_store', 'ice_Cream_desc', 'Enter_amount', 'payment_channel', 'your_location']

class Food_errand(forms.ModelForm):
    Food_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Food: description; Quantity(plate)", 'row':2}))
    class Meta:
        model =  Errand_service_PH
        fields = [ 'Food_Vendor', 'Food_description', 'description', 'Enter_amount', 'payment_channel', 'your_location']

class Other_errand(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Item description and specifications", 'row':2}))
    class Meta:
        model =  Errand_service_PH
        fields = [ 'description', 'Quantity', 'Enter_amount', 'payment_channel', 'your_location']

class Front_desk_pick(forms.ModelForm):
    class Meta:
        model = Front_desk_PH
        fields = ['customer_name', 'Customer_phone_number', 'item_description', 'delivery_destination', 'Reciever_phone_number', 'customer_location', 'Amount_Payable', 'Choice_for_TP', 'Note' ]

class Front_desk_errand(forms.ModelForm):
    class Meta:
        model = Front_desk_PH
        fields = ['customer_name', 'Customer_phone_number', 'Quantity', 'delivery_destination', 'item_description', 'Enter_amount', 'Delivery_Fee', 'Reciever_phone_number', 'Purchase_location', 'Receiver_name', 'Choice_for_TP', 'customer_location', 'Note']

####  UPDATE FORM  ######

class AdminAnonForm(forms.ModelForm):    
    class Meta:
        model = Anonymous
        fields = ['status', 'confirmed', 'Amount_Paid', 'receiver_name', 'receiver_address', 'Cancelation_Reason', 'customer_payment_method', 'receiver_contact', 'riders', ]

class adminformCash(forms.ModelForm): 
    class Meta:
        model = MakeRequestCash_PH
        fields = ['status', 'Amount_Paid', 'confirmed', 'Cancelation_Reason', 'riders']

class adminformShopping(forms.ModelForm): 
    class Meta:
        model = Shopping_PH
        fields = ['amount_paid', 'status', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded', 'confirmed', 'riders',]

class AdminErrandForm(forms.ModelForm):   
    class Meta:
        model = Errand_service_PH
        fields = ['status', 'confirmed', 'Amount_Paid', 'riders', 'profit' ]

class AdminFrontForm(forms.ModelForm):
    class Meta:
        model = Front_desk_PH
        fields = ['status', 'confirmed', 'Cancelation_Reason', 'customer_payment_method', 'riders', 'Amount_Paid', 'profit']