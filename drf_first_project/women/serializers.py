from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Women


# class WomenModel():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    date_create = serializers.DateTimeField(read_only=True)
    date_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.date_create = validated_data.get('date_create', instance.date_create)
        instance.date_update = validated_data.get('date_update', instance.date_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance


# def encode():
#     model = WomenModel('Vladiks', 'Content: proger')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json_data = JSONRenderer().render(model_sr.data)
#     print(json_data)


