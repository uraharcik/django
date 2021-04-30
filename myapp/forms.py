from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews, Ratting, RattingStar


class ReviewForm(forms.ModelForm):
    #Formular pentru adaugarea comentariilor
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ("email", "name", "text")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your email"}),
            "text": forms.Textarea(attrs={"class": "form-control", "rows": "4", "placeholder": "Comment"})
        }


class RattingForm(forms.ModelForm):

    star = forms.ModelChoiceField(
        queryset=RattingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Ratting
        fields = ("star",)