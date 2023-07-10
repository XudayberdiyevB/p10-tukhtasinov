from rest_framework import serializers

from sponsor.models import Sponsor


class SponsorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('fullname', 'phone', 'organization_name', 'amount')


class SponsorListSerializer(serializers.Serializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'phone', 'amount', 'spend_money', 'created_at', 'status')


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "is_organization", "organization_name")
