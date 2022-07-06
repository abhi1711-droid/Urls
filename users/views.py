from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth

from users.forms import SignupForm, UrlForm
from users.models import Url


@login_required
def index(request):
    current_user = request.user.id
    domain = request.build_absolute_uri('/')[:-1]
    five = Url.objects.filter(created_by=current_user).order_by('-created_at')[:5]
    form = UrlForm(request.POST or None)
    if form.is_valid():
        url = form.save(commit=False)
        url.created_by = request.user
        url.save()

        return render(request, "users/index.html", {'form': form, 'new': url, 'five': five, 'host': domain})
    return render(request, "users/index.html", {'form': form, 'new': None, 'five': five, 'host': domain})


@login_required
def search(request):
    return render(request, "users/search.html")


@login_required
def searchlink(request):
    if request.method == "POST":
        short = request.POST['short_link']
        link = short.split('/')
        search_url = link[-1]
        user_link = Url.objects.filter(short_link=search_url)[:1].get()
        print(user_link)
        return render(request, 'users/search.html', {'link': user_link})


@login_required
def listall(request):
    current_user = request.user.id
    domain = request.build_absolute_uri('/')[:-1]
    list_links = Url.objects.filter(created_by=current_user).all()
    return render(request, 'users/list.html', {'list': list_links, 'host': domain})


def root(request, short_link):
    url = get_object_or_404(Url, short_link=short_link)
    url.clicked()

    return redirect(url.original_link)


def login(request):
    return render(request, 'registration/login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('login')


class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"


