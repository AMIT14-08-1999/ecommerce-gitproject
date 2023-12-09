from . import views
from django.urls import path
urlpatterns = [
    path('register/',views.register,name='register'),
    path('me/',views.current_User,name='current_User'),
    path('me/update/',views.update_User,name='update_User'),
    path('forget_password/',views.forgot_password,name='forgot_password'),
    path('reset_password/<str:token>',views.reset_password,name='reset_password'),
]
