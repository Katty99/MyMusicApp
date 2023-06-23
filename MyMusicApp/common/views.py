from django.shortcuts import render, redirect

from MyMusicApp.account.forms import AccountForm
from MyMusicApp.account.models import Account
from MyMusicApp.albums.models import Album


# Create your views here.

def home_with_profile(request):
    account = Account.objects.first()
    albums = Album.objects.all()
    context = {"account": account, 'albums': albums}
    return render(request, template_name='common/home-with-profile.html', context=context)


def home_without_profile(request):
    account = Account.objects.first()
    if request.method == "GET":
        form = AccountForm()
    else:
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'account': account, 'form': form}
    return render(request, template_name='common/home-no-profile.html', context=context)


def home(request):
    account = Account.objects.first()
    if account:
        return home_with_profile(request)
    else:
        return home_without_profile(request)
