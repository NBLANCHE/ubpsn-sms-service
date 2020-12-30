from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from charity_user.views import CharityUserViewSet
from rest_framework.routers import DefaultRouter

from charity_user import views

router = DefaultRouter()
router.register(r"user", CharityUserViewSet)
urlpatterns = [
    # path(
    #     "<int:charity_user_pk>/subscribed_newsletter_topic/<int:newsletter_topic_pk>/",
    #     views.CharityUserSubscribedNewsletterTopicDetail.as_view(),
    # ),
]
urlpatterns += router.urls