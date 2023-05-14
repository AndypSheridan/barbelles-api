from django.urls import path
from profile import views


urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]
