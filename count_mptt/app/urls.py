from django.urls import path
from .views import TopicsView


urlpatterns = [
    path('topic/', TopicsView.as_view())
]