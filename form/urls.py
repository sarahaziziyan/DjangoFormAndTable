from django.urls import path, re_path, include
from . import views
from form import views as formapp_views



app_name='form'
urlpatterns = [
    re_path(r'^index/$', views.HelloView.as_view(), name='index'),
    # re_path(r'^form/$', views.showFormView.as_view(), name='form')
    # re_path(r'^$', views.showFormView.as_view(), name='form')
    re_path(r'^$', formapp_views.personalformRender, name='form'),
]

#{% url 'ticket:index' %}