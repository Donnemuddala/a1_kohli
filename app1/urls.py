from unicodedata import name
from urllib.parse import urlparse
from app1.views import a1_kohli
from django.urls import path
app_name='app1'
urlpatterns=[
    path('a1_kohli/',a1_kohli,name='a1_kohli'),
    ]
