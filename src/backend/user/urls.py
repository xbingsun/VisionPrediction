from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login_user', views.login_user, name='login_user'),
    path('login_admin', views.login_admin, name='login_admin'),
    path('add_user', views.add_user, name='add_user'),
    path('add_user_info', views.add_user_info, name='add_user_info'),
    path('modify_doc_pass', views.modify_doc_pass, name='modify_doc_pass'),
    path('get_visual_data', views.get_visual_data, name='get_visual_data'),
    path('get_user_info', views.get_user_info, name='get_user_info'),
    path('modify_user_pass', views.modify_user_pass, name='modify_user_pass'),
    path('get_prediction', views.get_prediction, name='get_prediction'),
    path('get_user_age', views.get_user_age, name='get_user_age'),
    path('get_stat', views.get_stat, name='get_stat'),
]