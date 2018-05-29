from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_lesson/$', views.add_lesson, name='add_lesson'),
	url(r'^register/$', views.register, name='register')
	]