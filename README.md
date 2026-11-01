# Bonnes Lectures

Application Django réalisée en TP de Framework Web à l’Université d’Orléans (2026–2027).
On peut consulter des livres et leurs auteurs, puis se connecter pour ajouter des livres et publier des avis notés de 1 à 5.

## Ce qui est fait

- Ajout, modification et suppression de livres, d’auteurs et d’avis.
- Connexion et déconnexion avec les comptes Django.
- Modification et suppression réservées au propriétaire ou à un administrateur.
- Pagination des livres et des avis ; page regroupant ses propres avis.
- Protection contre la suppression d’un auteur qui possède encore des livres.

Le projet utilise Python, Django, SQLite et Bootstrap 5 via django-bootstrap5.

## Lancer en local

Avec Python 3.10 ou plus récent, depuis la racine du dépôt :

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd bonnes_lectures
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000. Le compte créé permet de se connecter à l’application et à `/admin/`. Commencer par créer un auteur, puis un livre.

Sous Windows, remplacer l’activation par `.venv\Scripts\activate`.

La base démarre vide : les données et comptes utilisés pendant les TP ne sont pas inclus.
La clé Django est lue depuis `DJANGO_SECRET_KEY`, ou générée au démarrage pour le développement. Sans clé fixe, les sessions peuvent être invalidées au redémarrage. La configuration fournie sert au lancement local (`DEBUG=True`).

## Repères dans le code

- `bonnes_lectures/mainapp/` : modèles, formulaires, vues et pages HTML.
- `bonnes_lectures/mainapp/migrations/` : évolution de la base au fil des TP.
- `bonnes_lectures/bonnes_lectures/` : configuration et routes du projet.

Pour vérifier la configuration : `python manage.py check` depuis le dossier contenant `manage.py`. Le fichier de tests du TP ne contient pas encore de tests automatisés.

Hassan Slimani
