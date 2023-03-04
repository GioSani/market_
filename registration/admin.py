from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import User,Profile
@admin.register(User)
class RegistrationtAdmin(admin.ModelAdmin):
    list_display = ('id','email','uuid')

@admin.register(Profile)
class RegistrationtAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','uuid')
