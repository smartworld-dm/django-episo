from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^', views.index, name="brand_admin_index"),
	url(r'^login', views.login, name="brand_admin_login"),
	url(r'^dashboard', views.dashboard, name="brand_admin_dashboard"),
	url(r'^publish_article', views.publish_article, name="publish_article"),
	url(r'^creation/(?P<id>\d+)/', views.edit_article, name="edit_article"),
	url(r'^creation', views.new_article, name="new_article"),
	url(r'^save_article/(?P<id>\d+)/', views.update_article, name="update_article"),
	url(r'^save_article', views.save_article, name="save_article"),
	url(r'^file_upload', views.file_upload, name="file_upload"),
	url(r'^profile', views.profile, name="profile"),
]