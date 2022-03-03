from rest_framework import serializers
from apps.crud.models import Tutorial

class Tutorialserializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields =('id',
                 'title',
                 'description',
                 'published')
