from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_safe

from accounts.views import login
from .models import Movie, Genre
from .genre_info import GENRE
from django.core.paginator import Paginator
from django.http import JsonResponse
import random

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
@login_required
def recommended(request):
    me = request.user
    friends = me.followings.all()
    my_friends_likes=[]
    for friend in friends:
        if friend.like_movies.all():
            for friend_movie in friend.like_movies.all():
                if friend_movie not in my_friends_likes:
                    my_friends_likes.append(friend_movie)
    context = {
        'my_friends_likes': my_friends_likes,
    }
    return render(request, 'movies/recommended.html', context)

def search(request):
    questions = Movie.objects.all()
    q = request.GET.get('q', '')
    if q: 
        questions = questions.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    # paginator = Paginator(questions, 3)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
        'movies' : questions,
        'q' : q,
        # 'page_obj' : page_obj,
        'search_page' : True,
    }

    return render(request, 'movies/index.html', context)

@login_required
@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            liked = False
        else:
            movie.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'movie': movie,
        }
        return render(request, 'movies/detail.html', context)
    return redirect("accounts:login")


# def random_movie(request):
#     movies = Movie.objects.order_by('?')[:20]
#     moviesList = []

#     for movie in movies:
#         moviesList.append(
#             {
#                 'title': movie.title,
#                 'release_date': movie.release_date,
#                 'vote_average': movie.vote_average,
#                 'poster_path': movie.poster_path,
#             }
#         )

#     return render(request, 'movies/index.html', context)



def random_movie(request):
    movies = Movie.objects.order_by('?')[:20]
    moviesList = []

    for movie in movies:
        moviesList.append(
            {
                'title': movie.title,
                'release_date': movie.release_date,
                'vote_average': movie.vote_average,
                'poster_path': movie.poster_path,
            }
        )
    return JsonResponse(moviesList, safe=False)


    # mystery_movies= []
    # sf_movies = []
    # docu_movies= []
    # thriller_movies= []
    # comedy_movies=[]
    # family_movies = []
    # romance_movies= []


def christmas(request):
    movies_list = Movie.objects.all()
    state = request.GET.get('state')
    if state == 'alone':
        genre = 35
    elif state == 'couple':
        genre = 28
    elif state == 'freind':
        genre = 28
    elif state == 'family':
        genre = 28
    # genre = request.GET.get('genre_num')
    movies= movies_list.filter(genres=genre)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/christmas.html', context)

    