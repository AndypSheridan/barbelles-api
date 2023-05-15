from django.urls import path
from tutorials import views


urlpatterns = [
    path('tutorials/', views.TutorialList.as_view()),
    path('tutorials/<int:pk>', views.TutorialDetail.as_view()),
]