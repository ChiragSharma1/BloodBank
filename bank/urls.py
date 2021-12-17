from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('user/<int:userid>', views.get_user, name='user'),
    path('donarform/', views.donarform, name='donar_form')
]
