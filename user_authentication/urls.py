from django.urls import path
from .views import obtain_token

urlpatterns = [
    path('obtain_token/', obtain_token, name='obtain_token')
]
