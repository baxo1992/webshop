from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path("register/", views.register, name="register"),
]