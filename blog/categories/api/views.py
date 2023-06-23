from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializer import CatergorySerializer


class CategoryApiViewSet(ModelViewSet):
    serializer_class = CatergorySerializer
    queryset = Category.objects.all()

