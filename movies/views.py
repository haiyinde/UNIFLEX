from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from .genre_info import GENRE
from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    recommended_movies = Movie.objects.order_by('-pk')[:12]

    context = {
        'recommended_movies': recommended_movies,
    }
    return render(request, 'movies/recommended.html', context)

def search(request):
    questions = Movie.objects.all()
    q = request.GET.get('q', '')
    if q: 
        questions = questions.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    paginator = Paginator(questions, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : questions,
        'q' : q,
        'page_obj' : page_obj,
        'search_page': True,
    }

    return render(request, 'movies/index.html', context)

def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.user.filter(pk=request.user.pk).exists():
            movie.user.remove(request.user)
        else:
            movie.user.add(request.user)
        return redirect('movies:detail', movie_pk)
    return redirect('accounts:login')