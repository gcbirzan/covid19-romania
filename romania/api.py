from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control
from django.views.decorators.vary import vary_on_headers
from rest_framework import serializers, viewsets

from romania.models import DailyReport


class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = DailyReport


class DataViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = DailyReportSerializer
    queryset = DailyReport.objects.all().order_by('date')

    @method_decorator(cache_page(60 * 5, cache="default_pickle"))
    @method_decorator(cache_control(public=True, max_age=0, s_maxage=60))
    @method_decorator(vary_on_headers('Origin'))
    def list(self, *args, **kwargs):
        return super(DataViewset, self).list(*args, **kwargs)
