import django_filters
from django import forms
from .models import Product
#iexact , icontains
class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains',
                                     widget=forms.TextInput(attrs={'class': "form-control",
                                                                   'id': "table_filter"}))

    class Meta:
        model=Product
        fields=['name']