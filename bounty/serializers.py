from rest_framework import serializers
from bounty.models import Bounty, BountyItem, ChowBountyUser
        
class BountyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BountyItem
        fields = ('item_name', 'item_quantity')

class BountySerializer(serializers.ModelSerializer):
    cb_user = serializers.PrimaryKeyRelatedField(queryset=ChowBountyUser.objects.all())
    
    class Meta:
        model = Bounty
        fields = ('id', 'cb_user', 'price', 'creation_date', 'expiration_date', 'item_count', 'is_saved', 'is_claimed', 'is_requested', 'bountyitem_set')
        read_only_fields=('id')
        depth = 1
