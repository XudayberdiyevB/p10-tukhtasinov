from rest_framework import serializers

from sponsor.models import Sponsor


class SponsorSerializer(serializers.Serializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'phone', 'amount', 'spend_money', 'created_at', 'status')
