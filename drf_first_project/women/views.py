from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer
import sqlite3


class WomenAPIView(APIView):
    def get(self, request):
        women = Women.objects.all()
        return Response({'posts': WomenSerializer(women, many=True).data})

    def post(self, request):
        serialis = WomenSerializer(data=request.data)
        serialis.is_valid(raise_exception=True)
        serialis.save()
        return Response({'post': serialis.data})

    def put(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Women.objects.get(pk=pk)
        except Exception:
            return Response({'error': 'Object does not exist'})

        serialiser = WomenSerializer(data=request.data, instance=instance)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        return Response({'post': serialiser.data})

    def delete(self,request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Object does not exist'})

        try:
            instance = Women.objects.filter(id=pk)
        except Exception:
            return Response({'error': 'Object does not exist'})
        instance.delete()
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute('SELECT MAX(id) FROM women_women')
        last_id = cursor.fetchall()[0][0]
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=?", (int(last_id),))
        connection.commit()
        connection.close()
        return Response({'post': f"delete post: {str(pk)}"})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
