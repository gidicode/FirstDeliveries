#signaling for new users profile
import json
import base64
from .models import Anonymous, Customer, Delivered, MakeRequest, MakeRequestCash, Shopping, adminNotification 
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal
from django.core.mail import message, send_mail, EmailMultiAlternatives
from string import Template
from django.conf import settings
import requests


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance) # we want to run everytime a user is created
        add_items = Anonymous.objects.filter(email = instance.email)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.customer.save()
        
@receiver(post_save, sender=Delivered)
def Delivered_signals(sender, instance, created, **kwargs):
    if created:
        customer =Customer.objects.get(pk=instance.customer.id )
        cus = customer.delivered_set.all()

        customer.delivered_set.filter(order_id = instance.order_id).update(
                                title = 'Delivered!',
                                Message= f"Hello {instance.customer} Your parcel with the following refrence Number '{instance.order_id}' has been Delivered, Thanks for using our service.")
        print(instance.order_id)


@receiver(post_save, sender=MakeRequest)
def adminNotification11(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(pk=instance.customer.id )
        customer.adminnotification_set.filter(order_id = instance.order_id)
        
                        
@receiver(post_save, sender=MakeRequestCash)
def adminNotificationCash(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(pk=instance.customer.id )
        customer.adminnotification_set.filter(order_id = instance.order_id)

@receiver(post_save, sender=Shopping)
def adminNotificationShopping(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(pk=instance.customer.id )
        customer.adminnotification_set.filter(order_id = instance.order_id)

@receiver(post_save, sender=adminNotification)
def adminNotificationAnon(sender, instance, created, **kwargs):
    
    if created:
        def SendSms():
            username = 'gidis'
            password = "1299211??Gidi"
            url = "https://api.bulksms.com/v1/messages"
            link = f'http://127.0.0.1:4433/search/?order_id={instance.order_id}'
            sms_message = f"Your Request has been Created succesfully, visit link to check the status {link}"
            number = '+2347067320119'
            tokenid= '9944ED5D44E64014B84A22A6FA5BEA10-02-5'
            token_secret= 'sMjrbYJPPRbNpfvrccW1#EydjigFv'
            to_encode=tokenid + ":" + token_secret
            message_bytes = to_encode.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            port = 443

            payload = {
                'from':'Flls',
                "to" : [number],
                'body' : sms_message
                
                }
            
            header = {
                'Authorization': 'Basic'+ " " + base64_message,
                'Content-Type header':'application/json'
                }
            
            response = requests.post(url, headers=header, data=payload, )
            print(response.text)
            print(response)
            result = response.json()
            return result
        SendSms()

        my_email = 'usuugwo@gmail.com'
        email = instance.email
        items = instance.item_created
        date_created = instance.date_created
        Reference = instance.order_id
        print(Reference)
 
        subject, my_email, to=['Hello', my_email, email]
        text_content = "Dispatch Request Information"
        html_content ="""
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

            <head>
                <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <meta name="viewport" content="width=device-width">
                <!--[if !mso]><!-->
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <!--<![endif]-->
                <title></title>
                <!--[if !mso]><!-->
                <link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css">
                <link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css">
                <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
                <link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css">
                <!--<![endif]-->
                <style type="text/css">
                    body {
                        margin: 0;
                        padding: 0;
                    }

                    table,
                    td,
                    tr {
                        vertical-align: top;
                        border-collapse: collapse;
                    }

                    * {
                        line-height: inherit;
                    }

                    a[x-apple-data-detectors=true] {
                        color: inherit !important;
                        text-decoration: none !important;
                    }
                </style>
                <style type="text/css" id="media-query">
                    @media (max-width: 700px) {

                        .block-grid,
                        .col {
                            min-width: 320px !important;
                            max-width: 100% !important;
                            display: block !important;
                        }

                        .block-grid {
                            width: 100% !important;
                        }

                        .col {
                            width: 100% !important;
                        }

                        .col_cont {
                            margin: 0 auto;
                        }

                        img.fullwidth,
                        img.fullwidthOnMobile {
                            max-width: 100% !important;
                        }

                        .no-stack .col {
                            min-width: 0 !important;
                            display: table-cell !important;
                        }

                        .no-stack.two-up .col {
                            width: 50% !important;
                        }

                        .no-stack .col.num2 {
                            width: 16.6% !important;
                        }

                        .no-stack .col.num3 {
                            width: 25% !important;
                        }

                        .no-stack .col.num4 {
                            width: 33% !important;
                        }

                        .no-stack .col.num5 {
                            width: 41.6% !important;
                        }

                        .no-stack .col.num6 {
                            width: 50% !important;
                        }

                        .no-stack .col.num7 {
                            width: 58.3% !important;
                        }

                        .no-stack .col.num8 {
                            width: 66.6% !important;
                        }

                        .no-stack .col.num9 {
                            width: 75% !important;
                        }

                        .no-stack .col.num10 {
                            width: 83.3% !important;
                        }

                        .video-block {
                            max-width: none !important;
                        }

                        .mobile_hide {
                            min-height: 0px;
                            max-height: 0px;
                            max-width: 0px;
                            display: none;
                            overflow: hidden;
                            font-size: 0px;
                        }

                        .desktop_hide {
                            display: block !important;
                            max-height: none !important;
                        }
                    }
                </style>
                <style type="text/css" id="icon-media-query">
                    @media (max-width: 700px) {
                        .icons-inner {
                            text-align: center;
                        }

                        .icons-inner td {
                            margin: 0 auto;
                        }
                    }
                </style>
            </head>

            <body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #f9f9f9;">
                <!--[if IE]><div class="ie-browser"><![endif]-->
                <table class="nl-container" style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f9f9f9; width: 100%;" cellpadding="0" cellspacing="0" role="presentation" width="100%" bgcolor="#f9f9f9" valign="top">
                    <tbody>
                        <tr style="vertical-align: top;" valign="top">
                            <td style="word-break: break-word; vertical-align: top;" valign="top">
                                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#f9f9f9"><![endif]-->
                                <div style="background-color:#ff2b2b;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#ff2b2b;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 30px; width: 100%;" align="center" role="presentation" height="30" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="30" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <div class="img-container center autowidth" align="center" style="padding-right: 0px;padding-left: 0px;">
                                                            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img class="center autowidth" align="center" border="0" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/670631_653013/FLLS%20LOGO.png" alt="Yourlogo" title="Yourlogo" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 235px; display: block;" width="235">
                                                            <!--[if mso]></td></tr></table><![endif]-->
                                                        </div>
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 60px; width: 100%;" align="center" role="presentation" height="60" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="60" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 20px; padding-bottom: 20px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
                                                        <div style="color:#ffffff;font-family:Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:20px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: Georgia, Times, 'Times New Roman', serif; color: #ffffff; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 46px; line-height: 1.2; text-align: center; word-break: break-word; font-family: Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 55px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 46px;">Welocome to First Laurel Logistics</span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#d9e1ec;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.5;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; color: #d9e1ec; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 18px;">
                                                                <p style="margin: 0; font-size: 14px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 21px; margin-top: 0; margin-bottom: 0;">You are recieving this email because you requested for a dispatch rider.</p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 60px; width: 100%;" align="center" role="presentation" height="60" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="60" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 10px; width: 100%;" align="center" role="presentation" height="10" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="10" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:#09bbff;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#09bbff;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 0px; width: 100%;" align="center" role="presentation" height="0" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="0" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:transparent;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 40px; width: 100%;" align="center" role="presentation" height="40" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="40" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:transparent;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:20px; padding-bottom:30px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:20px; padding-bottom:30px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 0px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#ff0042;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:0px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="font-size: 12px; line-height: 1.2; color: #ff0042; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 12px; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin-top: 0; margin-bottom: 0;">&nbsp;</p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 10px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
                                                        <div style="color:#393d47;font-family:Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:5px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: Georgia, Times, 'Times New Roman', serif; color: #393d47; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 28px; line-height: 1.2; word-break: break-word; font-family: Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 34px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 28px;">Request with the following information;</span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#393d47;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.5;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; color: #393d47; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 18px;">
                                                                <p style="margin: 0; line-height: 1.5; word-break: break-word; font-size: 15px; mso-line-height-alt: 23px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 15px;">$description</span></p>
                                                                <p style="margin: 0; line-height: 1.5; word-break: break-word; font-size: 15px; mso-line-height-alt: 23px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 15px;"></span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 10px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
                                                        <div style="color:#393d47;font-family:Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:5px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: Georgia, Times, 'Times New Roman', serif; color: #393d47; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 14px; line-height: 1.2; word-break: break-word; font-family: Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 17px; margin-top: 0; margin-bottom: 0;"><strong><span style="font-size: 18px;">Reference Number:</span></strong></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#393d47;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.5;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; color: #393d47; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 18px;">
                                                                <p style="margin: 0; line-height: 1.5; word-break: break-word; font-size: 15px; mso-line-height-alt: 23px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 15px;">$reference</span></p>
                                                                <p style="margin: 0; line-height: 1.5; word-break: break-word; font-size: 15px; mso-line-height-alt: 23px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 15px;"></span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 5px; padding-bottom: 10px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
                                                        <div style="color:#393d47;font-family:Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:5px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: Georgia, Times, 'Times New Roman', serif; color: #393d47; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 14px; line-height: 1.2; word-break: break-word; font-family: Georgia, Times, 'Times New Roman', serif; mso-line-height-alt: 17px; margin-top: 0; margin-bottom: 0;"><strong><span style="font-size: 18px;">Date Created:</span></strong></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#393d47;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.5;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; color: #393d47; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 18px;">
                                                                <p style="margin: 0; line-height: 1.5; word-break: break-word; font-size: 15px; mso-line-height-alt: 23px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 15px;">$date</span></p>
                                                                <p style="margin: 0; line-height: 1.5; word-break: break-word; font-size: 15px; mso-line-height-alt: 23px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 15px;"></span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:transparent;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 40px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 5px; width: 100%;" align="center" role="presentation" height="5" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" height="5" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:#7c0524;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #760422;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#760422;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#7c0524;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:#760422"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:#760422;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:30px; padding-bottom:5px;background-color:#760422;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; background-color: #760422; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:30px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 20px; font-family: Georgia, 'Times New Roman', serif"><![endif]-->
                                                        <div style="color:#d9e1ec;font-family:'Bitter', Georgia, Times, 'Times New Roman', serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:20px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: 'Bitter', Georgia, Times, 'Times New Roman', serif; color: #d9e1ec; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; text-align: center; line-height: 1.2; word-break: break-word; font-family: Bitter, Georgia, Times, 'Times New Roman', serif; font-size: 20px; mso-line-height-alt: 24px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 20px;">To check&nbsp; for the status of your Request</span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <div class="button-container" align="center" style="padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://http://127.0.0.1:8000" style="height:19.5pt;width:125.25pt;v-text-anchor:middle;" arcsize="16%" strokeweight="0.75pt" strokecolor="#BCB081" fill="false"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ddd3a3; font-family:Arial, sans-serif; font-size:12px"><![endif]--><a href="http://http://127.0.0.1:8000" target="_blank" style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #ddd3a3; background-color: transparent; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; width: auto; width: auto; border-top: 1px solid #BCB081; border-right: 1px solid #BCB081; border-bottom: 1px solid #BCB081; border-left: 1px solid #BCB081; padding-top: 0px; padding-bottom: 0px; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;"><span style="padding-left:30px;padding-right:30px;font-size:12px;display:inline-block;letter-spacing:undefined;"><span style="font-size: 12px; line-height: 2; word-break: break-word; mso-line-height-alt: 24px;">VISIT US</span></span></a>
                                                            <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
                                                        </div>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:#7c0524;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#7c0524;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <table class="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" role="presentation" valign="top">
                                                            <tbody>
                                                                <tr style="vertical-align: top;" valign="top">
                                                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 30px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
                                                                        <table class="divider_content" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #BBBBBB; width: 100%;" align="center" role="presentation" valign="top">
                                                                            <tbody>
                                                                                <tr style="vertical-align: top;" valign="top">
                                                                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:#7c0524;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#7c0524;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#d9e1ec;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #d9e1ec; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 12px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 14px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 12px;">2021 © All Rights Reserved</span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                        <div style="color:#d9e1ec;font-family:Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #d9e1ec; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;">
                                                                <p style="margin: 0; font-size: 12px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 14px; margin-top: 0; margin-bottom: 0;"><span style="font-size: 12px;"><a href="http://www.example.com" target="_blank" rel="noopener" style="color: #d9e1ec;">Unsubscribe</a> | <a href="http://www.example.com" target="_blank" rel="noopener" style="color: #d9e1ec;">Manage Preferences</a></span></p>
                                                            </div>
                                                        </div>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <div style="background-color:transparent;">
                                    <div class="block-grid " style="min-width: 320px; max-width: 680px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                            <div class="col num12" style="min-width: 320px; max-width: 680px; display: table-cell; vertical-align: top; width: 680px;">
                                                <div class="col_cont" style="width:100% !important;">
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                        <!--<![endif]-->
                                                        <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top">
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td style="word-break: break-word; vertical-align: top; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px; text-align: center;" align="center" valign="top">
                                                                    <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                                                    <!--[if !vml]><!-->
                                                                    <table class="icons-inner" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation" valign="top">
                                                                        <!--<![endif]-->
                                                                        <tr style="vertical-align: top;" valign="top">
                                                                            <td style="word-break: break-word; vertical-align: top; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;" align="center" valign="top"><a href="https://www.designedwithbee.com/"><img class="icon" alt="Designed with BEE" src="https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/BeeProAgency/53601_510656/Signature/bee.png" height="32" width="null" align="center" style="border:0;"></a></td>
                                                                            <td style="word-break: break-word; font-family: Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif; font-size: 15px; color: #9d9d9d; vertical-align: middle; letter-spacing: undefined;" valign="middle"><a href="https://www.designedwithbee.com/" style="color:#9d9d9d;text-decoration:none;">Designed with BEE</a></td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if (!mso)&(!IE)]><!-->
                                                    </div>
                                                    <!--<![endif]-->
                                                </div>
                                            </div>
                                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                        </div>
                                    </div>
                                </div>
                                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!--[if (IE)]></div><![endif]-->
            </body>

            </html>
                """
        html_content = Template(html_content).substitute(description = instance.item_created, reference = Reference, date = date_created)

        msg = EmailMultiAlternatives(subject, text_content, my_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()