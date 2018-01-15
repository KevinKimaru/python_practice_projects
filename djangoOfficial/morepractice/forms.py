from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, BaseModelFormSet
from django.utils.translation import gettext_lazy as _

from .models import Author, Book

from django import forms


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        # exclude = ['name']
        # fields = '__all__'
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('<b>Some useful help text</b>'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20})
        }

class BaseAuthorFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.queryset = Author.objects.filter(name__startswith='k')
        # self.queryset = Author.objects.order_by('name')
        self.queryset = Author.objects.none()

    def clean(self):
        super().clean()

        for form in self.forms:
            name = form.cleaned_data['name'].upper()
            form.cleaned_data['name'] = name
            #update the instance value
            form.instance.name = name

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
        # localized_fields = ['name']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20)

# class AuthForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = '__all__'


