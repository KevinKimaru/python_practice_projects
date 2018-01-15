from datetime import datetime

from django.forms import modelformset_factory, modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, CreateView

from self_group.models import Member, Groupday, Unga


class MembersList(ListView):
    queryset = Member.objects.all()
    context_object_name = 'members'
    template_name = 'self_group/members.html'


class MemberCreate(View):
    MemberFormset = modelformset_factory(Member, fields='__all__', extra=1, can_delete=True)
    template_name = 'self_group/create_member.html'
    extra_forms = 1

    def post(self, request, *args, **kwargs):
        member_formset = self.MemberFormset(request.POST, queryset=Member.objects.none())
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(
                formset_dictionary_copy['form-TOTAL_FORMS']) + self.extra_forms
            member_formset = self.MemberFormset(formset_dictionary_copy)
        else:
            if member_formset.is_valid():
                member_formset.save()
                return HttpResponseRedirect(reverse('self_group:members'))
        return render(request, self.template_name, {'member_formset': member_formset})

    def get(self, request, *args, **kwargs):
        member_formset = self.MemberFormset(queryset=Member.objects.none())
        return render(request, self.template_name, {'member_formset': member_formset})

def day(request):
    DayForm = modelform_factory(Groupday, fields='__all__')
    current_date = timezone.datetime.now().date()

    if request.method == 'POST':
        day_form = DayForm(request.POST)
        if request.POST['date'] == str(current_date) and day_form.is_valid():
            day_form.save()
            return HttpResponseRedirect(reverse('self_group:members'))
    else:
        day_form = DayForm(initial={'date': str(current_date)})
    return render(request, 'self_group/group_day.html', {'form': day_form})

class UngaCreate(View):
    members_count = Member.objects.all().count()
    UngaFormset = modelformset_factory(Unga, fields=('member', 'has_paid', 'amount'), extra=members_count, can_delete=True)
    template_name = 'self_group/unga.html'
    extra_forms = 1
    current_date = str(timezone.datetime.now().date())

    def post(self, request, *args, **kwargs):
        unga_formset = self.UngaFormset(request.POST, queryset=Member.objects.none())
        print(request.POST)
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(
                formset_dictionary_copy['form-TOTAL_FORMS']) + self.extra_forms
            unga_formset = self.UngaFormset(formset_dictionary_copy)
        else:
            day = get_object_or_404(Groupday, date=self.current_date)
            if unga_formset.is_valid():
                ungas = unga_formset.save(commit=False)
                for unga in ungas:
                    unga.date = day
                    unga.save()
                return HttpResponseRedirect(reverse('self_group:members'))
        return render(request, self.template_name, {'unga_formset': unga_formset, 'date':self.current_date})

    def get(self, request, *args, **kwargs):
        unga_formset = self.UngaFormset(queryset=Member.objects.none())
        return render(request, self.template_name, {'unga_formset': unga_formset, 'date':self.current_date})


