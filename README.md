# 🎮 Gestionnaire de Collection de Jeux Vidéo

Une application **Django** moderne et intuitive permettant de gérer sa collection personnelle de jeux vidéo avec un design épuré et des fonctionnalités complètes.

---

## Objectif

Faciliter la gestion d'une collection de jeux vidéo pour un utilisateur lambda :

* **Ajout** de nouveaux jeux avec informations complètes
* **Consultation** de la liste
* **Recherche et filtrage avancés**
* **Modification/Suppression** avec validation

---

## Fonctionnalités

### 1️⃣ Ajouter un jeu

* Champs : Titre, Plateforme, Genre, Date de sortie, Note personnelle
* Validation :

  * Titre obligatoire
  * Note entre 0 et 10
  * Plateforme et genre prédéfinis

### 2️⃣ Liste des jeux

* Affichage sous forme de tableau ou cartes
* Informations visibles : Titre | Plateforme | Genre | Note

### 3️⃣ Filtres et recherche

* Filtrage par : Plateforme, Genre, Note minimale
* Recherche par mot-clé sur le titre

### 4️⃣ Modification et suppression

* Modification avec champs pré-remplis
* Suppression avec confirmation

---

## 📷 Captures d'écran

### Accueil
<img width="1920" height="1080" alt="Capture d’écran du 2025-08-15 11-49-47" src="https://github.com/user-attachments/assets/a5fb90b4-7207-4051-b2c4-e185ae9ebf19" />


### Liste des jeux
<img width="1920" height="1080" alt="Capture d’écran du 2025-08-15 11-49-54" src="https://github.com/user-attachments/assets/3d2e213c-d4a7-4a78-a117-2af5c748ecca" />



### Formulaire d’ajout
<img width="1920" height="1080" alt="Capture d’écran du 2025-08-15 11-50-00" src="https://github.com/user-attachments/assets/c2540606-e465-4b10-8e87-9182faa1b08f" />

---

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/Manoa1105/Collection-Jeux-Video.git
cd mon-projet-jeux

# 2. Créer un environnement virtuel
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Appliquer les migrations
python manage.py migrate

# 5. Lancer le serveur
django-admin runserver
```

---



## 👨‍💻 Auteur

Projet développé par **Manoa Rajaonah** dans le cadre d'un projet d'application Django.
