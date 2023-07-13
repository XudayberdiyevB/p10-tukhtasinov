from rest_framework import serializers

from sponsors.models import Sponsor


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "spend_money", "created_at", "status")


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", 'payment_type', "is_organization", "organization_name")


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", 'payment_type', "amount", "is_organization", "status", "created_at",
                  "organization_name")
        read_only = "id"
