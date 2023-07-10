from rest_framework import serializers
from .models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'id',
            'full_name',
            'phone',
            'amount',
            'is_organization',
            'status',
            'created_at',
            'organization_name'
        )
