from django.urls import path
from userprofile.views import display_userprofile, contacts

urlpatterns = [
    path('', display_userprofile, name='display_userprofile'),
    path('contacts/', contacts, name='contacts'),
]
