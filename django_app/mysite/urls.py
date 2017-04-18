from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'data', views.data, name='data'),
    # ex: /mysite/5/
    url(r'mysite/([0-9]+)/', views.detail, name='detail'),
]
