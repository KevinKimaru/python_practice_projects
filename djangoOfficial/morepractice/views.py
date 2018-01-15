from django.contrib.auth.forms import AdminPasswordChangeForm, AuthenticationForm, PasswordChangeForm, \
    PasswordResetForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.forms import modelform_factory, Textarea, modelformset_factory, inlineformset_factory
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .models import Book, Author, Writer, Publish, Student
from .forms import AuthorForm, BookForm, BaseAuthorFormSet, LoginForm


def thanks(request):
    return HttpResponse("Thankyou for filling the form.")


def oops(request):
    return HttpResponse("Thankyou for filling the form. However something went wrong. Perhaps your credentials.")


def index(request):
    # AuthorForm = modelform_factory(Author, fields=("name", "title", "birth_date"))
    # AuthorForm = modelform_factory(Author, form=AuthorForm, widgets={'title': Textarea()})
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            new_article = author_form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))
    else:
        author_form = AuthorForm()
    return render(request, 'morepractice/index.html', {'author_form': author_form})


def email_check(user):
    return user.email.endswith('@gmail.com')


@user_passes_test(email_check, login_url='morepractice/official_login')
def index_many(request):
    # if not request.user.email.endswith('@example.com'):
    #     return redirect('morepractice/login')


    AuthorFormSet = modelformset_factory(Author, fields=("name", "title", "birth_date"), extra=2,
                                         formset=BaseAuthorFormSet)  # , widgets={'name': Textarea()
    # AuthorFormSet = modelformset_factory(Author, form=AuthorForm)
    if request.method == 'POST':
        author_form_set = AuthorFormSet(request.POST)
        # author_form_set = AuthorFormSet(request.POST, queryset=Author.objects.none())
        if author_form_set.is_valid():
            author_form_set.save()
            # new_articles = author_form_set.save(commit=False)
            # for new_article in new_article:
            #     #do sth
            #     new_article.save()
            #     new_article.save_m2m()#if there is manytomany relationship
            return HttpResponseRedirect(reverse('morepractice:thanks'))
    else:
        author_form_set = AuthorFormSet()
        # author_form_set = AuthorFormSet(queryset=Author.objects.none())
        # author_form_set = AuthorFormSet(queryset=Author.objects.filter(name__startswith='k'))
    return render(request, 'morepractice/index_many.html', {'author_form_set': author_form_set})


@login_required(login_url='morepractice/login/', redirect_field_name='redirect_to')
def index_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))
    else:
        book_form = BookForm(initial={'name': 'Kevin'})
    return render(request, 'morepractice/index_book.html', {'book_form': book_form})


# @permission_required('morepractice.login_user')
def publish(request, writer_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('morepractice:login'))
    writer = Writer.objects.get(pk=writer_id)
    PublishInlineFormSet = inlineformset_factory(Writer, Publish, fields=('title',), extra=2)
    # # in case of many foreign keys in one model use fk_name='from_friendfields' which is the same name
    # # used as relsted name in the model Foreign mey field
    # FriendshipFormSet = inlineformset_factory(Friend, Friendship,
    #                                           fk_name='from_friendfields', fields=('to_friend', 'length_in_months'))
    if request.method == 'POST':
        formset = PublishInlineFormSet(request.POST, request.FILES, instance=writer)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))
    else:
        formset = PublishInlineFormSet(instance=writer)
    return render(request, 'morepractice/publish.html', {'formset': formset})


# # ===========================class based views
# # class MyFormView(LoginRequiredMixin, View):
# #     login_url = 'morepractice/login'
# #     redirect_field_name = 'redirect_to'
# class MyFormView(UserPassesTestMixin, View):
#     def test_func(self):
#         return self.request.user.email.endswith('@example.com')
#
#     login_url = 'morepractice/login'
#
#     form_class = AuthorForm
#     initial = {"name": "Kevin"}
#     template_name = 'morepractice/formview.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('morepractice:thanks'))
#         return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class MyFormView(View):
    login_url = 'morepractice/login'
    redirect_field_name = 'redirect_to'

    form_class = AuthorForm
    initial = {"name": "Kevin"}
    template_name = 'morepractice/formview.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))
        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('morepractice:thanks'))
            else:
                return HttpResponseRedirect(reverse('morepractice:oops'))
    else:
        form = LoginForm()
        return render(request, 'morepractice/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('morepractice:thanks'))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('morepractice:thanks'))

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'morepractice/change_password.html', {'form': form})


# def authm(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = AuthForm()
#     return render(request, 'morepractice/auth.html', {'form': form})

def change_admin_password(request):
    if request.method == 'POST':
        form = AdminPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))

    else:
        form = AdminPasswordChangeForm(request.user)
    return render(request, 'morepractice/change_admin_password.html', {'form': form})


def official_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))

    else:
        form = AuthenticationForm(request)
    return render(request, 'morepractice/official_login.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))

    else:
        form = PasswordResetForm(request.user)
    return render(request, 'morepractice/password_reset.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('morepractice:thanks'))

    else:
        form = UserCreationForm()
    return render(request, 'morepractice/create_user.html', {'form': form})


class BookList(ListView):
    model = Book
    context_object_name = 'my_books'


class BookDetail(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookListFiltered(ListView):
    # queryset = Book.objects.order_by('-name')
    # queryset = Book.objects.filter(name__startswith='The')
    queryset = Book.objects.filter(authors__name__startswith='W')
    context_object_name = 'my_books'


class BookListArgs(ListView):
    context_object_name = 'my_books'

    def get_queryset(self):
        self.author = get_object_or_404(Author, name=self.args[0])
        return Book.objects.filter(authors=self.author)


class AuthorDetailView(DetailView):
    # same as model = Author but you can do many things eg filter, order
    queryset = Author.objects.all()
    template_name = 'morepractice/authors.html'
    context_object_name = 'author'

    def get_object(self):
        object = super().get_object()
        object.last_accessed = timezone.now()
        object.save()
        return object


class BookClassView(FormView):
    template_name = 'bookclass.html'
    form_class = Book
    success_url = 'morepractice/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


# ==================================================
# @method_decorator(login_required, name='dispatch')
class StudentCreate(CreateView):
    login_url = 'morepractice/login'

    model = Student
    fields = ['name']



    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name']


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('morepractice:thanks')

