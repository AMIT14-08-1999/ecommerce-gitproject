from .models import *
from rest_framework import serializers


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductImages
        fields = "__all__"
        # fields =('name','price')

class ProductSerializer(serializers.ModelSerializer):
    images=ProductImagesSerializer(many=True,read_only=True)
    class Meta:
        model= Product
        # fields = "__all__"
        fields =('id','name','price','images','stock','description','brand','category','user')
        extra_kwargs={
            "name":{"required":True,"allow_blank":False},
            "category":{"required":True,"allow_blank":False},
            "brand":{"required":True,"allow_blank":False},
            "description":{"required":True,"allow_blank":False},
        }