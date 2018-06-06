from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
import logging
import os
import html

from articles.models import Article, Brand

logger = logging.getLogger(__name__)

def index(request):
	return render(request, 'brand_admin/index.html')

def login(request):
	if request.method == 'GET':
		return render(request, 'brand_admin/index.html')
	if request.method == 'POST':
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

def logout(request):
	auth_logout(request)
	return redirect('brand_admin_index')

@login_required(login_url='/brand-admin/login')
def dashboard(request):
	user = request.user
	brand = Brand.objects.filter(user=user).first()
	articles = Article.objects.filter(brand=brand).order_by('-creation_date')
	context = {'articles': articles}
	return render(request, 'brand_admin/dashboard.html', context)

@login_required(login_url='/brand-admin')
def new_article(request):
	return render(request, 'brand_admin/article.html')

@login_required(login_url='/brand-admin')
def edit_article(request, id):
	article = Article.objects.get(pk=id)
	content = html.escape(article.content)
	context = {'article': article, 'content': content}
	return render(request, 'brand_admin/article.html', context)

@login_required(login_url='/brand-admin')
def update_article(request, id):
	current_article = Article.objects.get(pk=id)
	title = request.POST.get('title', None)
	cover_image = request.FILES.get('cover-image', None)

	if cover_image:
		save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', cover_image.name)
		path = default_storage.save(save_path, cover_image)
		cover_image = cover_image.name
	else:
		cover_image = current_article.cover_image
	
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

	current_article.title = title
	current_article.brand = brand
	current_article.cover_image = cover_image
	current_article.member_name = member_name
	current_article.member_title = member_title
	current_article.attribute = attribute
	current_article.region = region
	current_article.category = category
	current_article.creation_date = creation_date
	current_article.content = content
	current_article.free_links = free_links
	current_article.save()
	return redirect('brand_admin_dashboard')

@login_required(login_url='/brand-admin')
def save_article(request):
	title = request.POST.get('title', None)
	cover_image = request.FILES.get('cover-image', None)

	if cover_image:
		save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', cover_image.name)
		path = default_storage.save(save_path, cover_image)
		cover_image = cover_image.name
	
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

@login_required(login_url='/brand-admin')
def file_upload(request):
	file = request.FILES['image']
	save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file.name)
	path = default_storage.save(save_path, file)
	return JsonResponse({"path": file.name})

@login_required(login_url='/brand-admin')
def profile(request):
	user = request.user
	brand = Brand.objects.filter(user=user).first()
	if request.method == 'GET':
		context = {'brand': brand}
		logger.error(brand.small_introduction)
		return render(request, 'brand_admin/profile.html', context)
	if request.method == 'POST':
		name = request.POST.get('name', None)
		name_slug = request.POST.get('name-slug', None)

		cover_image = request.FILES.get('cover-image', None)
		logo_image = request.FILES.get('logo-image', None)

		if cover_image:
			save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', cover_image.name)
			path = default_storage.save(save_path, cover_image)
			cover_image = cover_image.name
		else:
			cover_image = brand.cover_image

		if logo_image:
			save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', logo_image.name)
			path = default_storage.save(save_path, logo_image)
			logo_image = logo_image.name
		else:
			logo_image = brand.logo_image

		small_introduction = request.POST.get('small-introduction', None)
		introduction = request.POST.get('introduction', None)
		facebook_url = request.POST.get('facebook-url', None)
		twitter_url = request.POST.get('twitter-url', None)
		instagram_url = request.POST.get('instagram-url', None)
		company_name = request.POST.get('company-name', None)
		company_representative = request.POST.get('company-representative', None)
		company_address = request.POST.get('company-address', None)
		company_website = request.POST.get('company-website', None)
		company_founding_date = request.POST.get('company-founding-date', None)
		company_sales_offices = request.POST.get('company-sales-offices', None)
		company_introduction = request.POST.get('company-introduction', None)
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

		brand.name = name
		brand.name_slug = name_slug
		brand.cover_image = cover_image
		brand.logo_image = logo_image
		brand.small_introduction = small_introduction
		brand.introduction =introduction
		brand.facebook_url = facebook_url
		brand.twitter_url = twitter_url
		brand.instagram_url = instagram_url
		brand.company_name = company_name
		brand.company_representative = company_representative
		brand.company_address = company_address
		brand.company_website = company_website
		brand.company_founding_date = company_founding_date
		brand.company_sales_offices = company_sales_offices
		brand.company_introduction = company_introduction
		brand.free_links = free_links
		brand.save()
		
		return redirect('brand_admin_dashboard')

@login_required(login_url='/brand-admin')
def publish_article(request):
	article_id = request.POST.get('article_id', None)
	is_published = request.POST.get('is_published', None)
	article = Article.objects.get(pk=article_id)
	if is_published == 'true' : article.is_published = False
	else: article.is_published = True
	article.save()
	return JsonResponse({"is_published": is_published})