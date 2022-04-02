from django.urls import path
from . import views
name = "BloodBank"
urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('user/<int:userid>', views.get_user, name='user'),
    path('bank/<int:bankid>', views.get_bank, name="bank"),
    path('donarform/', views.donarform, name='donar_form'),
    path('emailSend/', views.emailSend, name='emailSend')
]
