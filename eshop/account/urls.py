from . import views
from django.urls import path
urlpatterns = [
    path('register/',views.register,name='register'),
    path('me/',views.current_User,name='current_User'),
    path('me/update/',views.update_User,name='update_User'),
]
