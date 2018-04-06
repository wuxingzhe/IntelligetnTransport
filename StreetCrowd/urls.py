from django.conf.urls import url

from . import views

app_name = 'StreetCrowd'
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^system/', views.index, name='index'),
    url(r'^upload/', views.upload_data),
    url(r'^help/',views.help)
]