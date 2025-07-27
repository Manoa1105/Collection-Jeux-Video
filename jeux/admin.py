from django.contrib import admin
from django.utils.html import format_html
from jeux.models import JeuVideo

@admin.register(JeuVideo)
class JeuVideoAdmin(admin.ModelAdmin):
    list_display = (
        'titre', 
        'plateforme', 
        'genres', 
        'date_de_sortie', 
        'note_personnelle', 
        'colored_note'
    )
    list_filter = ('plateforme', 'genres', 'date_de_sortie')
    search_fields = ('titre', 'plateforme', 'genres')
    ordering = ('-date_de_sortie',)
    list_per_page = 10

    fieldsets = (
        ("Informations Générales", {
            'fields': ('titre', 'plateforme', 'genres')
        }),
        ("Détails Supplémentaires", {
            'fields': ('date_de_sortie', 'note_personnelle'),
            'classes': ('collapse',),
        }),
    )

    def colored_note(self, obj):
        """Affiche la note colorée pour meilleure lisibilité"""
        color = (
            'green' if obj.note_personnelle >= 4 else
            'orange' if obj.note_personnelle >= 2 else
            'red'
        )
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.note_personnelle
        )
    colored_note.short_description = "Note visuelle"
