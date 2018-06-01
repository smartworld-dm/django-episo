from django.contrib.auth import login as auth_login
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
import logging
import os

from articles.models import Article, Brand

logger = logging.getLogger(__name__)

def index(request):
	return render(request, 'brand_admin/index.html')

def login(request):
	email_or_username = request.POST['email_or_username']
	password = request.POST['password']
	user = User.objects.filter(Q(username=email_or_username) | Q(email=email_or_username))
	if user.count() > 0:
		if user.first().check_password(password):
			auth_login(request, user.first())
			return redirect('brand_admin_dashboard')
		else:
			context = {"error": "Your username and password didn't match. Please try again."}
			return render(request, 'brand_admin/index.html', context)
	else:
		context = {"error": "Invalid username or email. Please try again."}
		return render(request, 'brand_admin/index.html', context)

def dashboard(request):
	user = request.user
	brand = Brand.objects.filter(user=user).first()
	articles = Article.objects.filter(brand=brand).order_by('-creation_date')
	context = {'articles': articles}
	return render(request, 'brand_admin/dashboard.html', context)

def new_article(request):
	return render(request, 'brand_admin/article.html')

def edit_article(request):
	return render(request, 'brand_admin/article.html')

def save_article(request):
	title = request.POST.get('title', None)
	# Upload file
	save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['cover-image'].name)
	path = default_storage.save(save_path, request.FILES['cover-image'])
	cover_image = request.FILES['cover-image'].name
	member_name = request.POST.get('member-name', None)
	member_title = request.POST.get('member-title', None)
	attribute = request.POST.get('attribute', None)
	region = request.POST.get('region', None)
	category = request.POST.get('category', None)
	creation_date = request.POST.get('creation_date', None)
	content = request.POST.get('content', None)
	free_link_1_anchor = request.POST.get('free-link-1-anchor', None)
	free_link_1_url = request.POST.get('free-link-1-url', None)
	free_link_2_anchor = request.POST.get('free-link-2-anchor', None)
	free_link_2_url = request.POST.get('free-link-2-url', None)
	free_link_3_anchor = request.POST.get('free-link-3-anchor', None)
	free_link_3_url = request.POST.get('free-link-3-url', None)
	free_links = {}
	if free_link_1_anchor and free_link_1_url: free_links[free_link_1_anchor] = free_link_1_url
	if free_link_2_anchor and free_link_2_url: free_links[free_link_2_anchor] = free_link_2_url
	if free_link_3_anchor and free_link_3_url: free_links[free_link_3_anchor] = free_link_3_url

	user = request.user
	brand = Brand.objects.filter(user=user).first()

	article = Article(
		title=title, 
		brand=brand,
		cover_image=cover_image,
		member_name=member_name,
		member_title=member_title,
		attribute=attribute,
		region=region,
		category=category,
		creation_date=creation_date,
		content=content,
		free_links=free_links
		)
	article.save()
	return redirect('brand_admin_dashboard')

def file_upload(request):
	file = request.FILES['image']
	save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file.name)
	path = default_storage.save(save_path, file)
	return JsonResponse({"path": file.name})

def publish_article(request):
	article_id = request.POST.get('article_id', None)
	is_published = request.POST.get('is_published', None)
	article = Article.objects.get(pk=article_id)
	if is_published == 'true' : article.is_published = False
	else: article.is_published = True
	article.save()
	return JsonResponse({"is_published": is_published})