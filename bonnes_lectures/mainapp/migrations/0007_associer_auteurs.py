from django.db import migrations


def relier_auteurs(apps, schema_editor):
    Book = apps.get_model("mainapp", "Book")
    Author = apps.get_model("mainapp", "Author")
    database = schema_editor.connection.alias
    books = Book.objects.using(database).all()

    for book in books:
        author, _ = Author.objects.using(database).get_or_create(
            first_name="",
            last_name=book.author_name,
        )
        book.author = author
        book.save(using=database, update_fields=["author"])


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_lien_auteur"),
    ]

    operations = [
        migrations.RunPython(relier_auteurs),
    ]