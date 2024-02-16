from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, TextField, SlugField, TextChoices, IntegerField, ImageField, URLField, \
    ManyToManyField, ForeignKey, CASCADE, DateField
from apps.shared.models import AbstractModel


class LanguageChoice(TextChoices):
    ENGLISH = "en", "English"
    FRANCE = "fr", "France"
    RUSSIAN = "ru", "Russian"
    ARABIC = "ab", "Arabic"
    UZBEK = "uz", "Uzbek"


class Book(AbstractModel):
    title = CharField(max_length=128)
    slug = SlugField(unique=True)
    description = TextField()
    published = DateField()
    isbn = CharField(max_length=128, unique=True)
    language = CharField(max_length=7, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH)
    page = IntegerField()
    cover = ImageField(upload_to="books/cover/%Y/%m/%d", default="book_cover.jpg")
    genre = ManyToManyField("books.BookGenre", "books")
    authors = ManyToManyField("books.BookAuthor", "books")


class BookAuthor(AbstractModel):
    first_name = CharField(max_length=56)
    last_name = CharField(max_length=56)
    birthdate = DateField()
    website = URLField()
    avatar = ImageField(upload_to="authors/avatar/%Y/%m/%d")
    about = TextField()


class BookGenre(AbstractModel):
    name = CharField(max_length=128)


class BookReview(AbstractModel):
    book = ForeignKey("books.Book", CASCADE, "reviews")
    user = ForeignKey("users.User", CASCADE, "reviews")
    body = TextField()
    rating = IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    like_count = IntegerField(default=0)
