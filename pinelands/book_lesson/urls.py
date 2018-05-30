from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_lesson/$', views.add_lesson, name='add_lesson'),
	url(r'^register/$', views.register, name='register'),
	url(r'^feedback/$', views.feedback_form, name='feedback'),
	url(r'^parent_register/$', views.parent_register, name='parent_register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^instrument_hire/$', views.instrument_hire, name='instrument_hire'),
	url(r'^logout/$', views.user_logout, name='logout')	
	]