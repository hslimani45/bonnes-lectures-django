from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('about', views.about),

    path('book/', views.books, name='books'),
    path('book/<int:book_id>', views.book, name='book'),
    path('new_book/', views.new_book, name='new_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/new_review/', views.new_review, name='new_review'),

    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),

    path('author/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('new_author/', views.new_author, name='new_author'),
    path('author/<int:author_id>/edit/', views.edit_author, name='edit_author'),
    path('author/<int:author_id>/delete/', views.delete_author, name='delete_author'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
]