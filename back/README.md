# 🛒 E-Commerce API

API RESTful pour une application e-commerce développée avec Django, Django REST Framework, JWT, Swagger, et Docker.

## 🔧 Fonctionnalités

- Authentification via JWT (inscription, connexion)
- Gestion des produits (CRUD avec permissions)
- Gestion du panier et des favoris (wishlist)
- Documentation Swagger automatisée
- Conteneurisation avec Docker + Docker Compose

---

## 🚀 Lancer le projet avec Docker

### Prérequis

- Docker
- Docker Compose

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/ecommerce-api.git
cd ecommerce-api

# 2. Lancer les conteneurs
docker-compose up --build

# 3. Appliquer les migrations
docker exec -it ecommerce-api-backend python manage.py migrate

# 4. (Optionnel) Créer un super utilisateur
docker exec -it ecommerce-api-backend python manage.py createsuperuser
