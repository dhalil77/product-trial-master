# 🛒 E-Commerce API

API RESTful pour une application e-commerce développée avec Django, Django REST Framework, JWT, Swagger, et Docker.

## 🔧 Fonctionnalités

- Authentification via JWT (inscription via /account, connexion via /token)
- Gestion des produits 
- Gestion des carts et des wishlist
- Documentation avec Swagger 
- Conteneurisation avec Docker + Docker Compose

---

## 🚀 Lancer le projet avec Docker

### Prérequis

- Docker
- Docker Compose

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/dhalil77/product-trial-master.git
cd product-trial-master

# 2. Lancer les conteneurs
docker-compose up --build
