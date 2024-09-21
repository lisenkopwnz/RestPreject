from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from animal1.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'title', 'content', 'time_create', 'time_update', 'is_published']

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.save()
        return instance

