from rest_framework import serializers

from sponsor.models import Sponsor


class SponsorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('fullname', 'phone', 'organization_name', 'amount')
