from rest_framework import serializers
from movies.models import Movie


# to convert from query_set to JSON object
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'desc', 'poster', 'video']
