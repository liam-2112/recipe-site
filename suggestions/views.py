from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Suggestion
from .forms import SuggestionForm

# Create your views here.


class SuggestionPage(TemplateView):
    """
    Displays suggestion page
    """
    template_name = 'suggestions/suggestions.html'


def suggestion_view(request):
    suggestions = Suggestion.objects.all().order_by("-created_on")
    suggestion_form = SuggestionForm()
    if request.method == "POST":
        Suggestion_form = SuggestionForm(data=request.POST)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.author = request.user
            suggestion.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Suggestion is submitted and awaiting approval')
            return redirect(reverse('suggestions')+'#top')

    context = {
        "suggestions": suggestions,
        "suggestion_form": suggestion_form,
    }

    return render(request, "suggestions/suggestions.html", context)

@login_required
def suggestion_edit(request, suggestion_id):
    """
    View to edit suggestions. Requires user to be logged in.
    """
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)

    if suggestion.author != request.user:
        messages.error(request, "You don't have permission to edit this suggestion.")
        return redirect('suggestions')

    if request.method == "POST":
        suggestion_form = SuggestionForm(request.POST, instance=suggestion)
        if suggestion_form.is_valid():
            updated_suggestion = suggestion_form.save(commit=False)
            updated_suggestion.approved = False
            updated_suggestion.save()
            messages.success(request, 'Suggestion updated and awaiting approval!')
            return redirect('suggestions')
    else:
        suggestion_form = SuggestionForm(instance=suggestion)

    template = 'suggestions/edit_suggestion.html'
    context = {
        'suggestion_form': suggestion_form,
        'suggestion': suggestion
    }
    return render(request, template, context)


def suggestion_delete(request, suggestion_id):
    """
    View to delete a suggestion
    """
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)

    if suggestion.author == request.user:
        suggestion.delete()
        messages.add_message(request,
                             messages.SUCCESS, 'Suggestion deleted successfully.')
    else:
        messages.add_message(
            request,
            messages.ERROR, 'Invalid request method for deleting suggestion.')

    return HttpResponseRedirect(reverse('suggestions'))