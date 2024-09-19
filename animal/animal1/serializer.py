from rest_framework import serializers

from animal1.models import Animal


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('title','cat_id')