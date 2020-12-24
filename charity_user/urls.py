from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from charity_user import views

urlpatterns = [
    path('', views.CharityUserList.as_view()),
    path('<int:pk>/', views.CharityUserDetail.as_view()),
    path('<int:charity_user_pk>/subscribed_newsletter_topic/<int:newsletter_topic_pk>/', views.CharityUserSubscribedNewsletterTopicDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
