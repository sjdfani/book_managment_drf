from django.urls import path
from .views import BookCreate, BookList, BookRetrieve, BookDestroy
app_name = 'book'

urlpatterns = [
    path('create/', BookCreate.as_view(), name='create'),
    path('', BookList.as_view(), name='list'),
    path('<int:pk>/', BookRetrieve.as_view(), name='retrieve'),
    path('delete/<int:pk>/', BookDestroy.as_view(), name='delete'),
]
