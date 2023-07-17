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

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = ("id", "full_name", "degree", "tuition_fee", "phone", "created_at", "university")


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ("id", "sponsor", "amount")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["sponsor"] = instance.sponsor.full_name
        return data


class StudentDetailSerializer(serializers.ModelSerializer):
    sponsors = StudentSponsorSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ("id", "full_name", "phone", "university", "degree", "total_sponsor_amount", "tuition_fee", "sponsors")
