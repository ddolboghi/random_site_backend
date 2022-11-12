from django.shortcuts import render
from .models import Question, Answer
from rest_framework import generics
from .serializers import QuestionSerializer, AnswerSerializer

class DetailQuestion(generics.RetrieveUpdateDestroyAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class DetailAnswer(generics.RetrieveUpdateDestroyAPIView):
  queryset = Answer.objects.all()
  serializer_class = AnswerSerializer