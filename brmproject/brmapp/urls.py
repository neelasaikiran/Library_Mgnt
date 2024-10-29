

from django.urls import path
from .views import home, addBookView, addBook, editBook, editBookView, deleteBookView

urlpatterns = [
    path("", home, name='home'),
    path('add-book/', addBookView, name='add-book-view'),
    path('add-book/add/', addBook, name='add-book'),
    path('edit-book/', editBookView, name='edit-book-view'),
    path('edit-book/edit/', editBook, name='edit-book'),
    path('delete-book/', deleteBookView, name='delete-book'),
]
