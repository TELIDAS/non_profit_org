from django_filters import rest_framework as filters

from news_npo.models import News


# class NewsFilter(filters.FilterSet):
#     title_filter = filters.CharFilter(field_name="title", lookup_expr='gte')
#
#     class Meta:
#         model = News
#         fields = ('title', 'title_filter')
