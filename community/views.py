from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from community.forms import CommentForm, ReviewForm
from community.models import Review, Comment

# Create your views here.
@require_safe
def index(request):
    if request.user.is_authenticated:
        reviews = Review.objects.order_by('-pk')
        context = {
            'reviews': reviews
        }
        return render(request, 'community/index.html', context)
    else:
        return redirect('accounts:login')


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_POST
def delete(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated:
        if request.user == review.user:
            review.delete()
            return redirect('community:index')
    return redirect('community:detail', review.review_pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('community:detail', review.pk)
            else:
                return redirect('community:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    context = {
        'review': review,
        'form':form,
    }
    return render(request, 'community/update.html', context)


@require_POST
def comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def comment_delete(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:detail', review_pk)


@login_required
@require_http_methods(['GET', 'POST'])
def comment_update(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('community:detail', review_pk)
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('community:index')
    context = {
        'comment': comment,
        'review': review,
        'form': form,
    }
    return render(request, 'community/comment_update.html', context)


@require_POST
def likes(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('community:detail', review.pk)
    return redirect('accounts:login')

@login_required
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'community/detail.html', context)
