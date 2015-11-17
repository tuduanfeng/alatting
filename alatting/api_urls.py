__author__ = 'tianhuyang'
from rest_framework.routers import DefaultRouter
from alatting_website.view.comment_viewset import CommentViewSet
from alatting_website.view.rating_viewset import RatingViewSet


router = DefaultRouter()
router.register(r'api/posters/(?P<poster_id>\d+)/comments', CommentViewSet, 'comment')
router.register(r'api/posters/(?P<poster_id>\d+)/ratings', RatingViewSet, 'rating')


urlpatterns = router.urls