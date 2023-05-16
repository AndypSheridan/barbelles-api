from django.urls import path
from tutorialcomments import views


urlpatterns = [
    path('tutorial-comments/', views.TutorialCommentList.as_view()),
    path('tutorial-comments/<int:pk>/', views.TutorialCommentDetail.as_view()),
]