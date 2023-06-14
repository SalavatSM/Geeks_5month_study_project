from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def product_list_api_view(request):
    """ 1 Step: Get data from DB """
    products = Product.objects.all()
    """ 2 Step: Reformat Queryset to list of dict objects """
    data = ProductSerializer(instance=products, many=True).data
    """ 3 Step: Return data as JSON file """
    return Response(data=data)


@api_view(['GET'])
def product_item_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(product, many=False).data
    return Response(data=data)


@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        'text': 'Hello World!',
        'int': 1000,
        'bool': True,
        "float": 2.99,
        'list': [1, 2, "adsfdas"],
        "dict": {
            "text": 'hello'
        }
    }
    return Response(data=dict_)

