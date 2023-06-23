from django.shortcuts import render, redirect

from MyMusicApp.account.models import Account
from MyMusicApp.albums.forms import AlbumForm, DeleteAlbumForm
from MyMusicApp.albums.models import Album


# Create your views here.

def add_album(request):
    account = Account.objects.first()
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form, 'account': account}
    return render(request, template_name='albums/add-album.html', context=context)


def details_album(request, pk):
    album = Album.objects.get(id=pk)
    account = Account.objects.first()
    context = {'album': album, 'account': account}
    return render(request, template_name='albums/album-details.html', context=context)


def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    account = Account.objects.first()
    if request.method == "GET":
        context = {'form': AlbumForm(initial=album.__dict__), 'account': account}
        return render(request, template_name='albums/edit-album.html', context=context)
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form': form, 'account': account}
            return render(request, template_name='albums/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "POST":
        album.delete()
        return redirect('home')
    form = DeleteAlbumForm(instance=album)
    context = {'form': form}
    return render(request, template_name='albums/delete-album.html', context=context)
