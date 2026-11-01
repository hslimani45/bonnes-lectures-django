from .models import Book, Review, Author
from .forms import BookForm, ReviewForm, AuthorForm
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.deletion import ProtectedError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def about(request):
    return HttpResponse(
        "Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2026."
    )


def welcome(request):
    return render(request, 'mainapp/welcome.html')

def books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'mainapp/books.html',
        {'page_obj': page_obj}
    )


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    reviews = book.reviews.all()
    paginator = Paginator(reviews, 5)

    page_number = request.GET.get("page")
    reviews_page = paginator.get_page(page_number)

    return render(
        request,
        'mainapp/book.html',
        {
            'book': book,
            'reviews_page': reviews_page
        }
    )

@login_required
def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book', book_id=book.id)
    else:
        form = BookForm()

    return render(request, 'mainapp/book_form.html', {'form': form})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        book.delete()
        return redirect('books')

    return render(
        request,
        'mainapp/book_confirm_delete.html',
        {'book': book}
    )


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book', book_id=book.id)
    else:
        form = BookForm(instance=book)

    return render(
        request,
        'mainapp/book_form.html',
        {'form': form}
    )


@login_required
def new_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()

            return redirect('book', book_id=book.id)
    else:
        form = ReviewForm()

    return render(
        request,
        'mainapp/review_form.html',
        {
            'form': form,
            'book': book
        }
    )


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if review.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect('book', book_id=review.book.id)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        'mainapp/review_form.html',
        {
            'form': form,
            'book': review.book
        }
    )


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if review.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    book = review.book

    if request.method == "POST":
        review.delete()
        return redirect('book', book_id=book.id)

    return render(
        request,
        'mainapp/review_confirm_delete.html',
        {'review': review}
    )


def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        'mainapp/authors.html',
        {'authors': authors}
    )


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    return render(
        request,
        'mainapp/author.html',
        {'author': author}
    )


@login_required
def new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()

            return redirect('author', author_id=author.id)
    else:
        form = AuthorForm()

    return render(
        request,
        'mainapp/author_form.html',
        {'form': form}
    )


@login_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if author.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            author = form.save()
            return redirect('author', author_id=author.id)
    else:
        form = AuthorForm(instance=author)

    return render(
        request,
        'mainapp/author_form.html',
        {'form': form}
    )


@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if author.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == "POST":
        try:
            author.delete()
            return redirect('authors')

        except ProtectedError:
            return render(
                request,
                'mainapp/author_confirm_delete.html',
                {
                    'author': author,
                    'error': "Cet auteur ne peut pas être supprimé car des livres lui sont associés."
                }
            )

    return render(
        request,
        'mainapp/author_confirm_delete.html',
        {'author': author}
    )

@login_required
def my_reviews(request):
    reviews = Review.objects.filter(user=request.user).order_by("-publication_date")

    return render(
        request,
        "mainapp/my_reviews.html",
        {"reviews": reviews}
    )