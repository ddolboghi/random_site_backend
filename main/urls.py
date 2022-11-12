from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main_page, name='index'),
    path('question/<int:pk>', views.DetailQuestion.as_view()),
    path('answer/<int:pk>', views.DetailAnswer.as_view()),
]
