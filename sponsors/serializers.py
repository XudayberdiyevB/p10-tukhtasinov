from rest_framework import serializers

from sponsors.models import Sponsor


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "spend_money", "created_at", "status")


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "is_organization", "organization_name")


class SponsorRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "status", "amount", "organization_name")
        read_only = ("id",)
