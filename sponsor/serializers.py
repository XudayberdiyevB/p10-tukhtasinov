from rest_framework import serializers

from sponsor.models import Sponsor


class SponsorListSerializer(serializers.Serializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'phone', 'amount', 'spend_money', 'created_at', 'status')


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "is_organization", "organization_name")


class SponsorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone', 'organization_name', 'amount')
