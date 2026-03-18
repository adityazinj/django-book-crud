from django.urls import path
from .views import book_create,home,book_detail,book_update,book_delete
urlpatterns = [
    path('',home,name='home'),
    path('book/detail/<int:pk>',book_detail,name="book-detail"),
    path('book/new/', book_create,name='book-create'),
    path('book/<int:pk>/edit',book_update,name="book-update"),
    path('book/<int:pk>/delete',book_delete,name="book-delete"),
]
