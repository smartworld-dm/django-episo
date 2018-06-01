from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
import logging

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

def publish_article(request):
	article_id = request.POST['article_id']
	is_published = request.POST['is_published']
	article = Article.objects.get(pk=article_id)
	if is_published == 'true' : article.is_published = False
	else: article.is_published = True
	article.save()
	return JsonResponse({"is_published": is_published})