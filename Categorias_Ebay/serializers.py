from rest_framework import serializers
from Categorias_Ebay.models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('BestOfferEnabled',
                   'AutoPayEnabled',
                    'CategoryID',
                    'CategoryLevel',
                    'CategoryName',
                    'CategoryParentID',
                    'LeafCategory')