from .views import CreateUserView
from django.urls import path, include, re_path
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r'users', CreateUserView)
urlpatterns = router.urls

urlpatterns += [
    re_path(r'^register/', CreateUserView.as_view()),
]
