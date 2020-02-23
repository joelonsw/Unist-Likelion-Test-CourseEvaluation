from django import forms
from .models import Course
from .models import Evaluation


# from multiselectfield import MultiSelectField


class SearchForm(forms.ModelForm):

    professor = forms.CharField(
        label=("professor"),
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "professor"}
        ),
    )

    code = forms.CharField(
        label=("code"),
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "code"}),
        # help_text=("Enter the title.")
    )

    title = forms.CharField(
        label=("title"),
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "type": "text", "placeholder": "title"}
        ),
        # help_text=("Enter user first and last name.")
    )

    CHOICES_semester = (("a", "20-1"),)
    semester = forms.ChoiceField(
        choices=CHOICES_semester,
        label=("semester"),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "list-group list-group-horizontal",
                "placeholder": "semester",
            }
        ),
    )

    class Meta:
        model = Course
        fields = ("professor", "title", "code", "semester")
