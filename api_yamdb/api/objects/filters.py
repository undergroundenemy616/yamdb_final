from django_filters import rest_framework as filters

from .models import Title


class TitleFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    year = filters.CharFilter(field_name="year", lookup_expr="iexact")
    genre = filters.CharFilter(field_name="genre__slug", lookup_expr="iexact")
    category = filters.CharFilter(field_name="category__slug", lookup_expr="iexact")

    class Meta:
        model = Title
        fields = ["name", "genre", "category", "year"]
