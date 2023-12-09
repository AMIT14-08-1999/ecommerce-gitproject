from .models import *
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = "__all__"


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductImages
        fields = "__all__"
        # fields =('name','price')

class ProductSerializer(serializers.ModelSerializer):
    images=ProductImagesSerializer(many=True,read_only=True)
    reviews=serializers.SerializerMethodField(method_name='get_reviews',read_only=True)
    class Meta:
        model= Product
        # fields = "__all__"
        fields =('id','name','price','reviews','images','stock','description','brand','category','user')
        extra_kwargs={
            "name":{"required":True,"allow_blank":False},
            "category":{"required":True,"allow_blank":False},
            "brand":{"required":True,"allow_blank":False},
            "description":{"required":True,"allow_blank":False},
        }
    def get_reviews(self,obj):
        reviews=obj.reviews.all()
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data