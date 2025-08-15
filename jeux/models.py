from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class JeuVideo(models.Model):
    titre = models.CharField(max_length=50)

    plateforme_choices = [
        ('PC', 'PC'),
        ('PS', 'Playstation'),
        ('XBOX', 'Xbox Series'),
        ('X360', 'Xbox 360'),
        ('SWITCH', 'Nintendo Switch'),
        ('WII', 'Nintendo Wii'),
        ('DS', 'Nintendo DS'),
        ('ANDROID', 'Android'),
        ('IOS', 'iOS'),
        ('MAC', 'Mac'),
        ('LINUX', 'Linux'),
        ('AUTRE', 'Autre'),
    ]
    plateforme = models.CharField(max_length=15, choices=plateforme_choices, default='AUTRE')

    genres_choices = [
        ('ACTION', 'Action'),
        ('AVENTURE', 'Aventure'),
        ('RPG', 'RPG'),
        ('STRATEGIE', 'Stratégie'),
        ('SIMULATION', 'Simulation'),
        ('SPORT', 'Sport'),
        ('COURSE', 'Course'),
        ('PUZZLE', 'Puzzle / Réflexion'),
        ('FPS', 'FPS (Shooter)'),
        ('HORREUR', 'Horreur'),
        ('PARTY', 'Party Game'),
        ('MUSIQUE', 'Musique / Rythme'),
        ('MMO', 'MMORPG'),
        ('SANDBOX', 'Sandbox / Construction'),
        ('EDUCATIF', 'Éducatif'),
        ('AUTRE', 'Autre')
    ]
        
    genres = models.CharField(max_length=20, choices=genres_choices, default='AUTRE')

    date_de_sortie = models.DateTimeField(null=True, blank=True)

    note_personnelle = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=False,
        null=True
    )

    #Ajout du champ pour la jaquette
    jaquette = models.ImageField(upload_to='jaquettes/', blank=True, null=True)

    def __str__(self):
        return f"{self.titre}, sortie en ({self.date_de_sortie})"
