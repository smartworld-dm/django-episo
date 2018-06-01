from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="brand_admin_index"),
	url(r'^login', views.login, name="brand_admin_login"),
	url(r'^dashboard', views.dashboard, name="brand_admin_dashboard"),
	url(r'^publish_article', views.publish_article, name="publish_article"),
]