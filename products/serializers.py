from rest_framework import serializers
from .models import Product, Category, Tag, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # tags = TagSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    # product_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        # deleted 'category, tags and product_reviews from fields
        fields = 'id title price category_name tags_name reviews'.split()
