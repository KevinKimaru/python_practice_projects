import datetime

from django.forms import formset_factory, BaseFormSet
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import send_mail

from .forms import NameForm, ContactForm, ArticleForm, BaseArticleFormSet, DrinkForm, BaseDrinkFormSet, BookForm


def thanks(request):
    return HttpResponse("Thankyou for filling the form.")


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('practice:thanks'))
    else:
        form = NameForm()

    return render(request, 'practice/name.html', {'form': form})


def article(request):
    ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet, validate_max=True, can_order=True, can_delete=True)
    BookFormSet = formset_factory(BookForm, extra=3)
    # formset.deleted_forms   formset.ordered_forms
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if article_formset.is_valid() and book_formset.is_valid():
            return HttpResponseRedirect(reverse('practice:thanks'))
    else:
        article_formset = ArticleFormSet(prefix='articles')
        book_formset = BookFormSet(prefix='books')

    return render(request, 'practice/article.html', {'formset': article_formset, 'book_formset': book_formset})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['kevinkimaru99@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(reverse('practice:thanks'))
    else:
        form = ContactForm()
    return render(request, 'practice/contacts.html', {'form': form})

def index(request):
    extra_forms = 2
    DrinkFormSet = formset_factory(DrinkForm, formset=BaseDrinkFormSet, extra=2, max_num=20)

    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
            formset = DrinkFormSet(formset_dictionary_copy)
        else:
            formset = DrinkFormSet(request.POST)
            if formset.is_valid():
                return HttpResponseRedirect(reverse('practice:thanks'))
    else:
        formset = DrinkFormSet(initial=[{'name': 1, 'size': 'm', 'amount': 1}])
    return render(request, 'practice/index.html',{'formset': formset})
























