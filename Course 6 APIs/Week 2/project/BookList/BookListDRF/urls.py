from django.urls import path
from .views import BookView,SingleBookView 

urlpatterns = [
    path('books/', BookView.as_view(), name='book-list'), 
    path('books/<int:pk>', SingleBookView.as_view()),
]
