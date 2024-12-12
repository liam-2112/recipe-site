from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm

# Create your views here.


class ReviewPage(TemplateView):
    """
    Displays review page
    """
    template_name = 'reviews/reviews.html'


def review_view(request):
    reviews = Review.objects.all().order_by("-created_on")
    review_form = ReviewForm()
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Suggestion is submitted and awaiting approval')
            return redirect(reverse('reviews')+'#top')

    context = {
        "reviews": reviews,
        "review_form": review_form,
    }

    return render(request, "reviews/reviews.html", context)

@login_required
def review_edit(request, review_id):
    """
    View to edit reviews. Requires user to be logged in.
    """
    review = get_object_or_404(Review, pk=review_id)

    if review.author != request.user:
        messages.error(request, "You don't have permission to edit this suggestion.")
        return redirect('reviews')

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            updated_review = review_form.save(commit=False)
            updated_review.approved = False
            updated_review.save()
            messages.success(request, 'Suggestion updated and awaiting approval!')
            return redirect('reviews')
    else:
        review_form = ReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'review_form': review_form,
        'review': review
    }
    return render(request, template, context)


def review_delete(request, review_id):
    """
    View to delete a review
    """
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request,
                             messages.SUCCESS, 'Suggestion deleted successfully.')
    else:
        messages.add_message(
            request,
            messages.ERROR, 'Invalid request method for deleting suggestion.')

    return HttpResponseRedirect(reverse('reviews'))