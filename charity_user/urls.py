from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from charity_user.views import CharityUserViewSet, SubscribedNewsletterTopicsViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from charity_user import views

router = routers.SimpleRouter()
router.register(r'user', CharityUserViewSet)

nested_router = routers.NestedSimpleRouter(router, r'user', lookup='user') 
nested_router.register(r'newsletter_topic', SubscribedNewsletterTopicsViewSet)

# urlpatterns = path('',
#     url(r'^', include(router.urls)),
#     url(r'^', include(nested_router.urls)),
# )

urlpatterns = [
    # path(
    #     "<int:charity_user_pk>/subscribed_newsletter_topic/<int:newsletter_topic_pk>/",
    #     views.CharityUserSubscribedNewsletterTopicDetail.as_view(),
    # ),
]
urlpatterns += router.urls
urlpatterns += nested_router.urls