from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.last_name


class Book(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="books",
    )
    title = models.CharField(max_length=300)
    publisher = models.CharField(max_length=200)
    year = models.IntegerField()
    isbn = models.CharField(max_length=20)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)
    cover_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    publication_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )