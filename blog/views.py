from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.reverse import reverse_lazy
from blog.forms import SignUPForm, SignInForm, CommentForm
from blog.models import *


# def home(request):
#     articles = Article.objects.all()
#     context = {
#         "articles":articles
#     }
#     return render(request,"blog/index.html",context)

# def category(request,pk):
#     article = Article.objects.filter(category_id=pk)
#     context = {
#         "articles": article,
#     }
#     return render(request,"blog/category.html",context)

# def search(request):
#     word = request.GET.get("q")
#     articles = Article.objects.filter(Q(title__icontains=word))
#     context = {
#         "articles": articles,
#     }
#     return render(request,"blog/search.html",context)

# def detail(request,pk):
#     article = Article.objects.get(pk=pk)
#     comments = Comment.objects.filter(article=article)
#     context ={
#         "article": article,
#         "comment_form": CommentForm(),
#         "comments": comments
#     }
#     return render(request,"blog/detail.html",context)

# def add_comment(request,pk):
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.user = request.user
#         comment.article = Article.objects.get(pk=pk)
#         comment.save()
#     else:
#         pass
#     return redirect("detail",pk)

# def signup(request):
#     if request.method == "POST":
#         form = SignUPForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect("home")
#     else:
#         form = SignUPForm()
#     context = {
#         "form":form
#     }
#     return render(request, "blog/signup.html",context)

# def signin(request):
#     if request.method == "POST":
#         form = SignInForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             return redirect("home")
#     else:
#         form = SignInForm()
#     context ={
#         "form":form
#
#     return render(request,"blog/signin.html",context)

# def signout(request):
#     logout(request)
#     return redirect("signin")





class Detail(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        comments = Comment.objects.filter(article=article)
        context["comments"] = comments
        context["comment_form"] = CommentForm
        return context

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/detail.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("detail",kwargs={"pk":self.kwargs['pk']})

class SignUp(CreateView):
    form_class = SignUPForm
    template_name = "blog/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

class SignIn(LoginView):
    template_name = "blog/signin.html"
    authentication_form = SignInForm
    def get_success_url(self):
        return reverse_lazy("home")

class SignOut(LogoutView):
    next_page = reverse_lazy("signin")

class Home(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"

class Category(Home):
    def get_queryset(self):
     return Article.objects.filter(category_id=self.kwargs['pk'])


class Search(Home):
     def get_queryset(self):
         word = self.request.GET.get("q")
         return Article.objects.filter(Q(title__icontains=word))




