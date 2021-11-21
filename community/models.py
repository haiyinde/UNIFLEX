from django.db import models
from django.conf import settings
from movies.models import Movie
# from accounts.models import User

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 리뷰 쓸 영화
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 리뷰 쓴 유저
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 게시글 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews' )

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # comment 쓸 review
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return self.content