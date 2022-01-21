from bye import views
from django.urls import path

#TEMPLATE TAGGING

app_name = 'bye'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]


