from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path("questions/", views.questionList, name="questions"),
    path("question-detail/<int:pk>/", views.questionDetail, name="question-detail"),
    path("question-create/", views.questionCreate, name="question-create"),
    path("question-update/<int:pk>/", views.questionUpdate, name="question-update"),
    path("question-delete/<int:pk>/", views.questionDelete, name="question-delete"),


    path("answers/", views.answerList, name="answers"),
    path("answer-detail/<int:pk>/", views.answerDetail, name="answer-detail"),
    path("answer-create/", views.answerCreate, name="answer-create"),
    path("answer-update/<int:pk>/", views.answerUpdate, name="answer-update"),
    path("answer-delete/<int:pk>/", views.answerDelete, name="answer-delete"),
]
