# SoftDesk Support API

Backend RESTful complet développé avec **Django** et **Django REST Framework**, destiné à la gestion de projets, de tickets ("issues") et de commentaires pour des équipes techniques.  
L’objectif est d’offrir une API sécurisée, performante, conforme RGPD et pensée pour minimiser l’impact environnemental (green code).

---

## 🚀 Fonctionnalités principales

### 🔐 Authentification & Permissions
- Authentification **JWT (JSON Web Token)** pour toutes les actions sensibles.
- Gestion complète des permissions :
  - Seuls les utilisateurs authentifiés accèdent à l’API.
  - Accès aux projets réservé aux contributeurs.
  - Seul l’auteur d’une ressource peut la modifier ou la supprimer.
- Respect des règles OWASP pour les API REST.

### 👤 Gestion des utilisateurs (User)
- Création / Modification / Suppression d’un utilisateur.
- Champs RGPD :
  - `can_be_contacted`
  - `can_data_be_shared`
- Vérification automatique de l’âge (≥ 15 ans).

### 📦 Gestion des projets (Project)
- Création de projet : titre, description, type (backend, frontend, iOS, Android).
- L’auteur est automatiquement ajouté comme **contributeur**.
- Accès réservé aux contributeurs du projet.

### 🤝 Gestion des contributeurs (Contributor)
- Liaison utilisateur ↔ projet via une table d’association.
- Un utilisateur peut contribuer à plusieurs projets.

### 🧾 Gestion des issues (Issue)
- Création de tickets pour un projet.
- Champs :
  - `priority` : LOW / MEDIUM / HIGH
  - `status` : To Do / In Progress / Finished
  - `tag` : BUG / TASK / FEATURE
- Assignation des issues uniquement aux contributeurs du projet.

### 💬 Gestion des commentaires (Comment)
- Commentaires attachés à une issue.
- Chaque commentaire possède un UUID unique.

### 🌱 Green code
- Pagination intégrée.
- Réponses légères (pas d’imbrication profonde).
- Optimisations des requêtes.

---

## 🧠 Stack technique

- Python 3.11+
- Django 5+
- Django REST Framework
- SimpleJWT
- Pipenv / Poetry (gestion des dépendances)
- Postman (tests manuels)

---

## 🛠️ Installation & exécution locale

### 1. Cloner le projet
```bash
git clone https://github.com/votre-pseudo/softdesk-support-api.git
cd softdesk-support-api
````
2. Installer les dépendances
Avec Pipenv :

```bash
pipenv install
pipenv shell
````
Ou avec pip :

````bash
pip install -r requirements.txt
````
3. Appliquer les migrations
````bash
Copier le code
python manage.py migrate
````
4. Lancer le serveur
````bash
Copier le code
python manage.py runserver
````
## 🔗 Endpoints principaux

### 🔐 Authentification

POST /api/auth/login/ → récupération du JWT

POST /api/auth/signup/ → création utilisateur

### 👤 Users
/api/users/

### 📦 Projects
/api/projects/

### 🤝 Contributors
/api/projects/{project_id}/contributors/

### 🧾 Issues
/api/projects/{project_id}/issues/

### 💬 Comments
/api/projects/{project_id}/issues/{issue_id}/comments/

### ✔️ Tests
Test des endpoints via Postman :

CRUD complet sur User

Gestion JWT

Création projet → ajout auto en contributeur

Issues assignées uniquement aux contributeurs du projet

Modifications réservées à l’auteur

Pagination activée

### 📐 Architecture du projet
````bash
softdesk-support-api/
│
├── softdesk/               # Configuration Django
│
├── users/                  # App utilisateurs (RGPD, JWT)
├── projects/               # App projets + contributeurs
├── issues/                 # App issues + commentaires
│
├── tests/                  # Tests unitaires
│
├── manage.py
├── requirements.txt
├── Pipfile / poetry.lock
├── README.md
└── .gitignore
````
### 📜 Licence
Projet publié sous licence MIT.

### 👤 Auteur
Développé par Jordan Lachaume

Développeur Backend Python / Django
