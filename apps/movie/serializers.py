from rest_framework import serializers
from .models import Movie
from rest_framework.response import Response


class CustomResponseSerializer(serializers.Serializer):
    def is_valid(self, raise_exception=False):
        valid = super().is_valid()

        if not valid and raise_exception:
            error_message = "Validation Error"
            error_detail = self.errors
            error_message += (
                f": {list(error_detail.keys())[0]} is required" if error_detail else ""
            )
            raise serializers.ValidationError(
                detail=error_detail,
                code="invalid",
                # status_code=400,
                # default_detail=error_message,
            )

        return valid


class MovieSerializer(
    serializers.ModelSerializer, CustomResponseSerializer
):  # create class to serializer model
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Movie
        fields = ("id", "title", "genre", "year", "creator")
