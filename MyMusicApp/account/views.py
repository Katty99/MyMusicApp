from django.shortcuts import render, redirect

from MyMusicApp.account.models import Account
from MyMusicApp.albums.models import Album


# Create your views here.

def profile_details(request):
    account = Account.objects.first()
    total_albums = len(Album.objects.all())
    context = {'account': account, 'total_albums': total_albums}
    return render(request, template_name='account/profile-details.html', context=context)


def profile_delete(request):
    account = Account.objects.first()
    albums = Album.objects.all()
    if request.method == 'POST':
        account.delete()
        albums.delete()
        return redirect('home')
    context = {'account': account, 'albums': albums}
    return render(request, template_name='account/profile-delete.html', context=context)
