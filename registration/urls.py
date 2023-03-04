from django.urls import path
from . import views


app_name = 'registration'

urlpatterns = [
    path('registration', views.registrationView, name='registration'),
    path('login',views.loginView,name='login'),
    path('activate/<str:uuid>',views.acitivate_url,name='activate'),
    path('logout/',views.logoutView,name='logout'),
    path('editProfile',views.editProfile,name='editProfile'),
    path('change_password',views.change_password,name='change_password')
    ]