from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    path('my_profile/', views.my_profile, name='my_profile'),
    path('update_profile/', views.UpdateProfile.as_view(), name='update_profile')
]