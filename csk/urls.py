from django.urls import path
from csk.views import*
app_name='Raj'
urlpatterns=[
    path('msd/',msd,name='msd'),
]