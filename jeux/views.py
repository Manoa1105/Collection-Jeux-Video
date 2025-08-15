from django.shortcuts import render, redirect, get_object_or_404
from jeux.models import JeuVideo
from .form import JeuVideoForm
from django.contrib import messages
from random import sample
from django.db.models import Count



def accueil(request):
    total_jeux = JeuVideo.objects.count()
    total_plateformes = JeuVideo.objects.values('plateforme').distinct().count()
    total_genres = JeuVideo.objects.values('genres').distinct().count()

    tous_les_jeux = list(JeuVideo.objects.all())
    jeux_affiches = sample(tous_les_jeux, min(7, len(tous_les_jeux)))

    return render(request, 'accueil.html', {
        'total_jeux': total_jeux,
        'total_plateformes': total_plateformes,
        'total_genres': total_genres,
        'jeux': jeux_affiches,
    })

# Ajouter un jeu
def ajouter_jeu(request):
    if request.method == 'POST':
        form = JeuVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Le jeu a bien été ajouté !")
            return redirect('list_jeux')
    else:
        form = JeuVideoForm()
    return render(request, 'ajouter_jeu.html', {'form': form})

# Lister les jeux avec filtres
def list_jeux(request):
    plateforme = request.GET.get('plateforme')
    genre = request.GET.get('genre')
    note_min = request.GET.get('note_min')
    recherche = request.GET.get('recherche', '')

    jeux = JeuVideo.objects.all()

    if plateforme:
        jeux = jeux.filter(plateforme=plateforme)
    if genre:
        jeux = jeux.filter(genres=genre)
    if note_min:
        jeux = jeux.filter(note_personnelle__gte=note_min)
    if recherche:
        jeux = jeux.filter(titre__icontains=recherche)

    context = {
        'jeux': jeux,
        'plateformes': [pf[0] for pf in JeuVideo.plateforme_choices],
        'genres': [g[0] for g in JeuVideo.genres_choices],
        'notes': list(range(1, 11)),
    }
    return render(request, 'list_jeux.html', context)

# Modifier un jeu
def modifier_jeu(request, id):
    jeu = get_object_or_404(JeuVideo, pk=id)
    if request.method == 'POST':
        form = JeuVideoForm(request.POST, request.FILES, instance=jeu)
        if form.is_valid():
            form.save()
            messages.success(request, f"Le jeu « {jeu.titre} » a bien été modifié.")
            return redirect('list_jeux')
    else:
        form = JeuVideoForm(instance=jeu)
    return render(request, 'ajouter_jeu.html', {'form': form, 'modifier': True})

# Supprimer immédiatement un jeu
def supprimer_jeu(request, id):
    jeu = get_object_or_404(JeuVideo, pk=id)
    jeu.delete()
    messages.success(request, f"Le jeu « {jeu.titre} » a été supprimé avec succès.")
    return redirect('list_jeux')

# Confirmation de suppression
def confirmer_suppression(request, pk):
    jeu = get_object_or_404(JeuVideo, pk=pk)
    if request.method == "POST":
        jeu.delete()
        messages.success(request, f"Le jeu « {jeu.titre} » a été supprimé.")
        return redirect('list_jeux')

    jeux = JeuVideo.objects.all()
    return render(request, 'list_jeux.html', {
        'jeux': jeux,
        'jeu': jeu,
        'confirm_delete': True,
        'plateformes': ['PC', 'PS', 'XBOX', 'SWITCH', 'AUTRE'],
        'genres': ['ACTION', 'SPORT', 'AVENTURE', 'RPG', 'AUTRE'],
        'notes': list(range(1, 11)),
    })
