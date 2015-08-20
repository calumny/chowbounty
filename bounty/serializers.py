from rest_framework import serializers
from bounty.models import Bounty, BountyItem, ChowBountyUser

class BountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bounty
        fields = ('price', 'creation_date', 'expiration_date', 'item_count', 'is_saved', 'is_claimed', 'is_requested')