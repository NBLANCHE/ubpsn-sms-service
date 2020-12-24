from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from message import views

urlpatterns = [
    path("", views.MessageList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
