from django.urls import path, re_path, include
from . import views
from form import views as formapp_views



app_name='form'
urlpatterns = [
    re_path(r'^index/$', views.HelloView.as_view(), name='index'),
    # re_path(r'^$', formapp_views.personalformRender, name='form'),
    re_path(r'^$', formapp_views.saveAndShowPersonel, name='form'),
]

#{% url 'ticket:index' %}