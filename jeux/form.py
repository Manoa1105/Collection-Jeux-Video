from django.forms import ModelForm, TextInput, Select, DateInput, NumberInput, FileInput
from .models import JeuVideo

class JeuVideoForm(ModelForm):
    class Meta:
        model = JeuVideo
        fields = ['titre', 'plateforme', 'genres', 'date_de_sortie', 'note_personnelle', 'jaquette']
        widgets = {
            'titre': TextInput(attrs={
                'placeholder': 'Ex : The Witcher 3',
                'autofocus': 'autofocus',
                'class': 'w-full px-4 py-2 bg-gray-900 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-netflixRed'
            }),
            'plateforme': Select(attrs={
                'class': 'w-full px-4 py-2 bg-gray-900 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-netflixRed'
            }),
            'genres': Select(attrs={
                'class': 'w-full px-4 py-2 bg-gray-900 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-netflixRed'
            }),
            'date_de_sortie': DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 bg-gray-900 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-netflixRed'
            }),
            'note_personnelle': NumberInput(attrs={
                'min': 0,
                'max': 10,
                'step': 1,
                'class': 'w-full px-4 py-2 bg-gray-900 text-white border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-netflixRed'
            }),
            'jaquette': FileInput(attrs={
                'class': 'w-full text-white file:bg-netflixRed file:text-white file:px-4 file:py-2 file:rounded-lg file:border-none file:hover:bg-red-700 transition'
            }),
        }
