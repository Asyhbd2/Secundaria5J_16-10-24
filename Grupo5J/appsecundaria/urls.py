from django.urls import path
from appsecundaria import views

urlpatterns = [
    path("",views.index_vista,name="Index_vista"),
]