from django.urls import path
from . import views

urlpatterns = [
    path('question/<int:pk>', views.DetailAlldata.as_view()),
    path('result/<int:pk>', views.DetailResult.as_view()),
]