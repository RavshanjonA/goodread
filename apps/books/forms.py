from django.forms import ModelForm, IntegerField, Widget, Textarea
from apps.books.models import BookReview


# class Textarea(Widget):
#     template_name = "django/forms/widgets/textarea.html"
#
#     def __init__(self, attrs=None):
#         # Use slightly better defaults than HTML's 20x2 box
#         default_attrs = {"cols": "10", "rows": "3"}
#         if attrs:
#             default_attrs.update(attrs)
#         super().__init__(default_attrs)


class AddBookReviewForm(ModelForm):
    rating = IntegerField(min_value=1, max_value=5)
    body = Textarea(attrs={"rows": "3"})

    class Meta:
        model = BookReview
        fields = ("body", "rating")
