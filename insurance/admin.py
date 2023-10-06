from django.contrib import admin

# Register your models here.
from .models import Service_Provider, Customer, Policy, Payment

class Service_ProviderAdmin(admin.ModelAdmin):
    list_display = ("name","service", "contact","gender","location")

admin.site.register(Service_Provider, Service_ProviderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name","customer_contact","policy" "Service_Provider","service_date","service_recieved")

admin.site.register(Customer)

class PolicyAdmin(admin.ModelAdmin):
    list_display = ("policy_name","Service_Provider", "benefits","lapse_period","cost")

admin.site.register(Policy, PolicyAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_date","policy","customer","amount_paid")

admin.site.register(Payment, PaymentAdmin)