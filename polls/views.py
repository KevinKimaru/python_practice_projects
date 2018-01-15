from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

from polls.models import Question, Choice
from django.template import loader
from django.shortcuts import  get_object_or_404, render
from django.urls import reverse
from django.views import generic


# def index(request):
#     latest_qustion_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join(q.question_text for q in latest_qustion_list)
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_qustion_list
#     }
#     return HttpResponse(template.render(context, request))


# def index(request):
#     latest_qustion_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_qustion_list}
#     return render(request, 'polls/index.html', context)



# def detail(request, question_id):
#     return HttpResponse("You are looking at question %s" % question_id)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return last 5 published excluding those to be published in the future"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """ Excludes any questions that aren't published yet. """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.detailView):
    model = Question
    template_name = 'polls/results.html'

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You didn\'t select a choice.'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        #  with POST data. This prevents data from being posted twice if a
        #  user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
