from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from newsletter_topic.views import NewsletterTopicViewSet, NewsletterTopicMessageViewSet

router = DefaultRouter()
router.register(r"topic", NewsletterTopicViewSet)
router.register(r"topic_message", NewsletterTopicMessageViewSet)
urlpatterns = []
urlpatterns += router.urls