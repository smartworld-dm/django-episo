from django.shortcuts import render
from django.http import HttpResponse
from collections import namedtuple
import logging
import json

from articles.models import Article, Brand

logger = logging.getLogger(__name__)

def index(request):
	return render(request, 'articles/show_brand.html', {"a":"a"})

def landing(request):
	articles = Article.objects.filter(is_featured=True, is_published=True)
	top6_articles = Article.objects.filter(is_published=True).order_by('-creation_date')
	top6_brands = Brand.objects.order_by('-creation_date')
	context = {'articles': articles, 'top6_articles': top6_articles, 'top6_brands': top6_brands}
	return render(request, 'articles/landing.html', context)

def show(request, id):
	article = Article.objects.get(pk=id)
	same_brand_articles = Article.objects.filter(is_published=True, brand = article.brand).exclude(pk=article.id).order_by('-creation_date')[:2]
	context = {'article': article, 'same_brand_articles': same_brand_articles}
	return render(request, 'articles/show.html', context)

def show_brand(request, name):
	brand = Brand.objects.filter(name=name).first()
	top3_articles = Article.objects.filter(is_published=True, brand=brand).order_by('-creation_date')[:3]
	logger.error(top3_articles)
	context = {'brand': brand, 'top3_articles': top3_articles}
	return render(request, 'articles/show_brand.html', context)