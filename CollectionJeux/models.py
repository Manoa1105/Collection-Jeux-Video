from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class JeuVideo(models.Model):
    titre = models.CharField(max_length = 50)
    plateforme = [
        ('PC', 'PC'),
        ('PS', 'Playstation'),
        ('XBOX', 'Xbox'),
        ('SWITCH', 'switch'),
        ('AUTRE', 'autre')
    ]

    GENRES = [
        ('ACTION', 'Action'),
        ('SPORT', 'Sport'),
        ('AVENTURE', 'Aventure'),
        ('RPG', 'RPG'),
        ('AUTRE', 'Autre'),
    ]

    genres = models.CharField(
        max_length=10,
        choices=GENRES,
    )

    date_de_sortie = models.DateTimeField()

    note_personnelle =  models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=False,
        null=True
    )

    def __str__(self):
        return f"{self.titre}, sortie en ({self.date_de_sortie})"

