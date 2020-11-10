from app.views import QuizView, QuizDetaliedView, SubmissionView
from django.urls import path

urlpatterns = [
url(r'api_token',obtain_jwt_token, name='api-token' ),
    url(r'refersh_api_token',refresh_jwt_token, name='refresh-api-token' ),
    path(r'quiz/', QuizView.as_view(), name="quiz"),
    path(r'quiz/<int:pk>/', QuizDetaliedView.as_view(), name="quiz-detail"),
    path(r'quiz/submission/', SubmissionView.as_view(), name="submission"),
]