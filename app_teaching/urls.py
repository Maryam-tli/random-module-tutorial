from django.urls import path
from app_teaching.views import *

urlpatterns = [
    path('', index_view, name='index'),
]