from django import forms

from MyMusicApp.albums.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist_name', 'genre', 'description', 'image', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album'}),
            'artist_name': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'placeholder': 'Genre'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'})
        }
        labels = {
            "image_url": "Image URL",
            "artist_name": "Artist",
            "album_name": "Album Name",
        }


class DeleteAlbumForm(AlbumForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
