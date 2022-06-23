from django.urls import path
from app.views import *

urlpatterns = [
    # some basic query
    path('Return_Queryset/', Return_Queryset),
    path('No_Return_Queryset/', No_Return_Queryset),
]