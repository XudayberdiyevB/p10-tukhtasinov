from rest_framework import serializers

from students.models import Student, StudentSponsor


class StudentListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student, StudentSponsor
        fields = ('full_name', 'degree', 'tuition_fee', 'university', 'amount')


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student, StudentSponsor
        fields = ('id', 'full_name', 'degree', 'tuition_fee', 'created_at', 'university', 'amount')
        read_only_fields = ('id',)
