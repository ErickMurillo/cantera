from django.shortcuts import render

# Create your views here.
def index (request, template='ForumIndex.html'):
	return render(request,template,locals())

def detail (request, template = 'ForumDetail.html'):
	return render(request,template,locals())