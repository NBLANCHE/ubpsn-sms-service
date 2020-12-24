from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from newsletter_topic import views

urlpatterns = [
    path('', views.NewsletterTopicList.as_view()),
    path('<int:pk>/', views.NewsletterTopicDetail.as_view()),
    path('<int:pk>/message/', views.NewsletterTopicMessageList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
