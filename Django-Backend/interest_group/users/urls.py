from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    InterestListCreateView,
    InterestDetailView,
    AcceptInterestView,
    RejectInterestView,
    UserDetailView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/<str:username>/", UserDetailView.as_view(), name="user-profile"),
    path("interests/", InterestListCreateView.as_view(), name="interests-list-create"),
    path("interests/<int:pk>/", InterestDetailView.as_view(), name="interests-detail"),
    path(
        "interest/<int:pk>/accept/",
        AcceptInterestView.as_view(),
        name="interesr-accept",
    ),
    path(
        "interest/<int:pk>/reject/",
        RejectInterestView.as_view(),
        name="interesr-reject",
    ),
]
