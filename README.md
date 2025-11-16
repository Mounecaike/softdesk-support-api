# SoftDesk Support API

Backend RESTful développé avec Django REST Framework pour la gestion de projets, de tickets et de commentaires entre utilisateurs (style bug tracker B2B).

## 🚀 Fonctionnalités
- Authentification JWT
- Gestion des utilisateurs (RGPD compliant)
- Gestion des projets, contributeurs, issues et commentaires
- Permissions et accès basés sur les rôles
- Pagination et principes de green code

## 🧠 Stack technique
- Python 3.11+
- Django 5.x
- Django REST Framework
- SimpleJWT
- Pipenv ou Poetry

## 🛠️ Installation locale
```bash
git clone https://github.com/tonpseudo/softdesk-support-api.git
cd softdesk-support-api
pipenv install
python manage.py migrate
python manage.py runserver
