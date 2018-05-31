from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import logging
import json

from articles.models import Article, Brand

logger = logging.getLogger(__name__)

def index(request):
	articles = Article.objects.filter(is_published=True).order_by('-creation_date')
	paginator = Paginator(articles, 2)
	page = request.GET.get('page')
	articles_page = paginator.get_page(page)
	context = {'articles': articles_page, 'page_cnt': range(articles_page.paginator.num_pages)}
	return render(request, 'articles/article_list.html', context)

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

def index_brand(request):
	brands = Brand.objects.order_by('-creation_date')
	paginator = Paginator(brands, 4)
	page = request.GET.get('page')
	brands_page = paginator.get_page(page)
	context = {'brands': brands_page, 'page_cnt': range(brands_page.paginator.num_pages)}
	return render(request, 'articles/brand_list.html', context)

def terms(request):
	return render(request, 'articles/terms.html')

def privacy(request):
	return render(request, 'articles/privacy.html')

def contact(request):
	return render(request, 'articles/contact.html')

def search(request):
	q = request.GET.get('q', None)
	if q in [None]:
		return render(request, 'articles/search.html')
	elif q in ['']:
		return render(request, 'articles/search_noquery.html')
	else:
		articles = Article.objects.filter(Q(title__contains=q) | Q(content__contains=q) | Q(member_name__contains=q) | Q(brand__name__contains=q)).order_by('-creation_date')
		paginator = Paginator(articles, 2)
		page = request.GET.get('page')
		articles_page = paginator.get_page(page)
		context = {'articles': articles_page, 'page_cnt': range(articles_page.paginator.num_pages), 'q': q}
		return render(request, 'articles/search_query.html', context)