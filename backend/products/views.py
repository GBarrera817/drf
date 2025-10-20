from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404

from .models import Product
from .serializers import ProductSerializer


# Create your views here.


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)

        # Adding custom data
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title

        serializer.save(content=content)

        # send a Django signal


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):

    # in detail view we have 1 single item to retrieve

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):

    # in detail view we have 1 single item to retrieve

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content: 
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):

    # in detail view we have 1 single item to retrieve

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        
        # instance
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):

    '''
    Not gonna use this method
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        # url_args??
        # get request -> detail view
        if pk is not None:
            # detail view

            """
            This is the common way to get the specific item
            """
            # queryset = Product.objects.filter(pk=pk)
            
            # if not queryset.exists():
            #     raise Http404

            obj = get_object_or_404(Product, pk=pk)  # pk=pk is the lookup field_name = field_value
            data = ProductSerializer(obj, many=False).data

            return Response(data)
        
        # list view
        queryset = Product.objects.all() # qs
        data = ProductSerializer(queryset, many=True).data

        return Response(data)

    if method == 'POST':
        # create an item

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title

            serializer.save(content=content)

            return Response(serializer.data)
        
        return Response({'invalid': 'not a good data'}, status=400)