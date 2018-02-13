from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choix, Question


class IndexView(generic.ListView):
    template_name = 'sondages/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'sondages/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'sondages/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choix = question.choix_set.get(pk=request.POST['choix'])
    except (KeyError, choix.DoesNotExist):
        return render(request, 'sondages/detail.html', {
            'question': question,
            'error_message': "You didn't select a choix.",
        })
    else:
        selected_choix.votes += 1
        selected_choix.save()
        return HttpResponseRedirect(reverse('sondages:results', args=(question.id,)))
