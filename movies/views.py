from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_safe, require_http_methods

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
# @require_http_methods(['GET','POST'])
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
        'friends': friends,
        'my_friends_likes': my_friends_likes,
    }
    return render(request, 'movies/recommended.html', context)


def search(request):
    questions = Movie.objects.all()
    q = request.GET.get('q', '')
    if q: 
        questions = questions.filter(title__icontains=q)

    context = {
        'movies' : questions,
        'q' : q,
        # 'page_obj' : page_obj,
        'search_page' : True,
    }

    return render(request, 'movies/index.html', context)

@login_required
# @require_POST
@require_http_methods(['GET', 'POST'])
def likes(request, movie_pk):
    # if request.user.is_authenticated:
    if request.method == 'POST':
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
        return redirect('movies:detail', movie_pk)
    # login ??? next??????????????? ?????? url??? ???????????????(GET)

    elif request.method == 'GET':
        return redirect('movies:detail', movie_pk)
    # return render(request, 'movies/detail.html', context)
    # return redirect("accounts:login")


def christmas(request):
    movies_list = Movie.objects.all()
    state = request.GET.get('state')
    if state:
        # 12-??????, 10749-?????????, 878-SF, 80-??????, 53-?????????, 35-?????????, 28-??????, 27-??????, 18-?????????, 14-?????????
        if state == 'alone':
            # ????????? - 35
            genre = 35
            humor = '???????????? ????????? ???????????????!????'
        elif state == 'couple':
            # ?????????-10749
            genre = 10749
            humor = '????????? ????????? ?????? ??????????????'
        elif state == 'friend':
            # SF - 878
            genre = 878
            humor = '????????? ?????? SF ?????????! ????'
        elif state == 'family':
            # ?????? - 10751
            genre = 10751
            humor = '????????? ??? ??? ?????? ?????? ??????! ????'
        else:
            return render(request, 'movies/christmas.html')

        movie_genres = movies_list.filter(genres=genre)
        # ???????????? 6????????? ????????? ????????????!
        movies = movie_genres.order_by('?')[:6]
        context = {
            'movies': movies,
            'humor': humor,
            'state': state,
        }
        return render(request, 'movies/christmas.html', context)
    return render(request, 'movies/christmas.html')
    

def random_movie(request):
    movies = Movie.objects.order_by('?')[:4]
    moviesList = []
    for movie in movies:
        if movie.overview == "":
            movie.overview = "????????? ???????????? ???????????? ????"
        moviesList.append(
            {
                'title': movie.title,
                'rating': movie.vote_average,
                'background': movie.poster_path,
                'synopsis': movie.overview[:170],
                'movie_pk': movie.pk,
            }
        )
    return JsonResponse(moviesList, safe=False)
