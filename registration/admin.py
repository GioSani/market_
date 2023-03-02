from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import User
@admin.register(User)
class RegistrationtAdmin(admin.ModelAdmin):
    list_display = ('id','email','uuid')
