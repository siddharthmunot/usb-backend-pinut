from django.conf.urls import url

from . import views

urlpatterns = [
	url (r'^$', views.index, name='index'),
	url (r'^change_data/$', views.change_data, name='changedata'),
	url (r'^change_logo/$', views.change_logo, name='changelogo'),
	url (r'^change_apk/$', views.change_apk, name='changeapk'),
	url (r'^captive_display/$', views.captive_display, name='captivedisplay')
]