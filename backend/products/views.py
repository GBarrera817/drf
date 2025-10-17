from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


# Create your views here.


class ProductCreateAPIView(generics.CreateAPIView):
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

product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):

    # in detail view we have 1 single item to retrieve

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()
