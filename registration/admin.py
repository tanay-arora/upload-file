from django.contrib import admin
from .models import attende, participants, startup, stay_informed, subscriber, transaction, users

@admin.register(stay_informed)
class stay_informedAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

@admin.register(subscriber)
class subscriberAdmin(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(attende)
class attendeAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','contact','email','tshirt_size']

@admin.register(participants)
class participantAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','contact','email','tshirt_size']

@admin.register(startup)
class startupAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','company_category','industry']

@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ['id','username']

@admin.register(transaction)
class transactionAdmin(admin.ModelAdmin):
    list_display = ['id','ticketid']