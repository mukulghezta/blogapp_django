from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import CreateArticle
from django.contrib.auth.decorators import login_required
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

def test(request):
	return render(request, 'articles/test.html')

'''
# Function View for article list
def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', { 'articles':articles })
'''

# Class Based View for article list
class article_list(ListView):
	template_name = 'articles/article_list.html'
	model = Article
	queryset = Article.objects.all()

'''
# Function View for article detail
def article_detail(request, id):
	#return HttpResponse(slug)
	article = Article.objects.get(id=id)
	return render(request, 'articles/article_detail.html', { 'article':article })
'''

# Class Based View for article detail
class article_detail(LoginRequiredMixin, DetailView):
	template_name = 'articles/article_detail.html'
	model = Article

	def get_object(self):
		id = self.kwargs.get('id')
		return get_object_or_404(Article, id=id)

'''
# Function View for article create
@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method == "POST":
		form = CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			#save article to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')
	else:
		form = CreateArticle()
	return render(request, 'articles/article_create.html', { 'form':form })
'''


# Class Based View for article create
class article_create(CreateView):
	template_name = 'articles/article_create.html'
	model = Article
	form_class = CreateArticle
	queryset = Article.objects.all()

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
'''
	def test_func(self):
		article = self.get_object()
		if self.request.user = article.author:
			return True
		return False
'''

'''
def article_edit(request, id):
	article = Article.objects.get(id=id)
	form = CreateArticle(request.POST, instance=article)
	return render(request, "articles/article_edit.html", {'article':article})
'''

def article_update(request, id):
	article = Article.objects.get(id=id)
	form = CreateArticle(instance=article)
	if request.method == "POST":
		form = CreateArticle(request.POST, instance=article)
		if form.is_valid():
			form.save()
			return redirect('articles:list')
	return render(request, 'articles/article_edit.html', {'article':article})

def article_delete(request, id):
	article = Article.objects.get(id=id)
	article.delete()
	return redirect('articles:list')