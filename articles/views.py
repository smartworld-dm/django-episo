from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': 'a'}
	return render(request, 'articles/index.html', context)