from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('<username>/', ProfileDetailView.as_view(), name='detail')
]