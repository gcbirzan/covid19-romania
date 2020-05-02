from django.contrib import admin

# Register your models here.
from romania.models import CountyData, DailyReport, County


@admin.register(DailyReport)
class DataAdmin(admin.ModelAdmin):
    pass


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    pass


@admin.register(CountyData)
class CountyDataAdmin(admin.ModelAdmin):
    pass
