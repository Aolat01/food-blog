from django.urls import path
from .views import SignUpView, ProfileView, editProfile

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView, name='profile'),
    path('edit_profile/<int:user_id>/', editProfile, name='edit_profile'),
]
