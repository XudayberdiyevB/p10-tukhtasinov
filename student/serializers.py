from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'full_name',
            'degree',
            'tuition_fee',
            'created_at',
            'university'
            )
