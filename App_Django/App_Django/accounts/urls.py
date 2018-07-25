from django.urls import path
from App_Django.accounts import views

urlpatterns = [

    path(r"novo-usuario/", views.add_User, name ="add_user"),
    path(r"login-usuario/", views.user_login, name ="user_login"),
    path(r"logout-usuario/", views.user_logout, name ="user_logout"),
    path(r"change-password/", views.change_password, name ="change_password")




]