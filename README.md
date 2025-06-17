# 🛒 MyStore - Projet Django eCommerce

Ce projet est une boutique en ligne développée avec Django 5.0.6.  
Il permet à des utilisateurs de s’inscrire, se connecter, gérer leurs adresses, naviguer dans des produits, ajouter au panier et passer commande avec simulation de paiement (Stripe test).

---

## 🚀 Fonctionnalités principales

- Authentification (inscription, connexion, déconnexion)
- Gestion des utilisateurs et adresses
- Catalogue produits (collections, catégories)
- Panier (session)
- Comparateur & wishlist
- Commande & checkout avec Stripe (mode test)
- Dashboard utilisateur
- Interface d'administration Django

---

## 🧰 Technologies

- Python 3.12
- Django 5.0.6
- SQLite (par défaut)
- Stripe (paiement)
- Bootstrap 5 (front-end)
- HTML / CSS / JS

---

## ⚙️ Installation locale

1. **Cloner le projet**


git clone https://github.com/votre-utilisateur/mystore.git
cd mystore

Créer un environnement virtuel

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Installer les dépendances

pip install -r requirements.txt
Appliquer les migrations
python manage.py migrate


Créer un superutilisateur (admin)
python manage.py createsuperuser


Lancer le serveur

python manage.py runserver
Accéder ensuite à : http://localhost:8000

💳 Test des paiements Stripe
Utilisez la carte suivante pour simuler un paiement réussi :

Numéro : 4242 4242 4242 4242

Date d’expiration : 12/34

CVC : 123

Autres cartes de test disponibles ici : https://stripe.com/docs/testing

📁 Structure des dossiers

accounts/ : gestion utilisateurs

dashboard/ : espace utilisateur

shop/ : produits, panier, commandes, paiement

templates/ : templates HTML

static/ : fichiers CSS/JS/images (non inclus ici)

📌 À faire / améliorations possibles
Ajouter un système de recherche/filtrage

Ajouter des notifications par email

Ajouter la gestion des stocks

Responsive design plus avancé



