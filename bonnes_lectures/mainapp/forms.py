from django.forms import ModelForm
from .models import Book, Review, Author


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "author",
            "title",
            "publisher",
            "year",
            "isbn",
            "backCover",
            "cover",
            "cover_url",
        ]

        labels = {
            "author": "Auteur",
            "title": "Titre",
            "publisher": "Maison d'édition",
            "year": "Année",
            "isbn": "ISBN",
            "backCover": "Texte de présentation",
            "cover": "Couverture",
            "cover_url": "URL de la couverture",
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["body", "rating"]


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]