from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .filters import ProductsFilter
from .models import Product
from rest_framework.response import Response
from .serializer import ProductSerializer
# Create your views here.
@api_view(['GET'])
def get_products(request):
    filterset=ProductsFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    resPerPage=2
    count=filterset.qs.count()
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage
    queryset=paginator.paginate_queryset(filterset.qs,request)
    setializer = ProductSerializer(queryset,many=True)
    return Response({
        "count":count,
        "resPerPage":resPerPage,
        "products":setializer.data
    })
@api_view(['GET'])
def get_product(request,pk):
    product = get_object_or_404(Product,id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response({
        "product":serializer.data,
    })