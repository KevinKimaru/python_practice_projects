import datetime
from django import forms
from django.forms import formset_factory, BaseFormSet


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

class BaseArticleFormSet(BaseFormSet):
    def clean(self):
        """Checks that no two articles have the same name"""
        if any(self.errors):
            #Don't bother validating the formset unless each form is valid on its own
            return
        titles = []
        for form in self.forms:
            title = form.cleaned_data['title']
            if title in titles:
                raise forms.ValidationError("Articles in a set must have distinct titles")
            titles.append(title)

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["my field"] = forms.CharField()

class BookForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

# ArticalFormSet = formset_factory(ArticleForm, extra=2, max_num=2)
# formset = ArticalFormSet(initial=[
#     {
#         'title': 'Power of django',
#         'pub_date': datetime.datetime.now(),
#     }
# ])
# USAGE IN VIEWS
# ArticalFormSet(request.POST, initial=[
#             {
#                 'title': 'Power of django',
#                 'pub_date': datetime.datetime.now(),
#             }
#         ])


# ArticalFormSet = formset_factory(ArticleForm)
# data = {
#     'form-TOTAL_FORMS': '2',
#     'form-INITIAL-FORMS': '0',
#     'form-MAX_NUM_FORMS': '',
#     'form-0-title': 'Test',
#     'form-0-pub_date': '1904-06-16',
# }
# formset = ArticalFormSet(data)
# formset.has_changed()
DRINKS = ((None, 'Please select a drink type'), (1, 'Mocha'), (2, 'Espresso'), (3, 'Latte'))
SIZES = ((None, 'Please select a drink size'), ('s', 'Small'), ('m', 'Medium'), ('1', 'Large'))
class DrinkForm(forms.Form):
    name = forms.ChoiceField(choices=DRINKS, initial=0)
    size = forms.ChoiceField(choices=SIZES, initial=0)
    amount = forms.ChoiceField(choices=[(None, 'Amount of drinks')] + [(i, i) for i in range(1, 10)])

class BaseDrinkFormSet(BaseFormSet):
    def clean(self):
         # check errors in dictionary first, if there are errors , no point in validating further
        if any(self.errors):
            return
        name_size_tuples = []
        for form in self.forms:
            name_size = (form.cleaned_data['name'], form.cleaned_data['size'])
            if name_size in name_size_tuples:
                raise forms.ValidationError("""Ups! You have multiple %s %s items in your order,
                 keep one and increase the amount""" % (dict(SIZES)[name_size[1]], dict(DRINKS)[int(name_size[0])]))
            name_size_tuples.append(name_size)





















