from django.shortcuts import render
from rest_framework import generics
from app.serailizers import QuizListSerializer, SubmissionSerializer, QuizSerializer
from app.models import Quiz, Submission


class QuizView(generics.ListAPIView):
    serializer_class = QuizListSerializer
    queryset = Quiz.objects.all()


class QuizDetaliedView(generics.RetrieveAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class SubmissionView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
