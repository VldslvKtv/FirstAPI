from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
import sqlite3


# реализация через ViewSet
# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

    # переопределение метода get ( но в urls у router.register нужно будет указать basename='women'
    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return Women.objects.all()[:3]
    #     return Women.objects.filter(pk=pk)

    # добавляем новый маршрут
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cts = Category.objects.get(pk=pk)
    #     return Response({'categories': cts.name})

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(id) FROM women_women')
    last_id = cursor.fetchall()[0][0]
    cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=?", (int(last_id),))
    connection.commit()
    connection.close()
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
