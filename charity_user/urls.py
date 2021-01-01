from charity_user.views import CharityUserViewSet, SubscribedNewsletterTopicsViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r"user", CharityUserViewSet)

nested_router = routers.NestedSimpleRouter(router, r"user", lookup="user")
nested_router.register(r"newsletter_topic", SubscribedNewsletterTopicsViewSet)

urlpatterns = []
urlpatterns += router.urls
urlpatterns += nested_router.urls
