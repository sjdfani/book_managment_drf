from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView
from .models import BookModel
from .serializer import BookSeializer, BookSeializerCreate
from .permissions import IsStaff, IsSuperUser


class BookList(ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSeializer
    permission_classes = []


class BookCreate(CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSeializer
    permission_classes = [IsSuperUser, IsStaff]


class BookRetrieve(RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSeializer
    permission_classes = []


class BookDestroy(DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSeializer
    permission_classes = [IsSuperUser, IsStaff]
