from django.contrib import admin
from .models import Clothing,Rates

class Ratesinlines(admin.TabularInline):
    model= Rates
    extra = 1
    readonly_fields =['date_created']
@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['name','price','size','type','average_rate']
    search_fields = ['name']
    list_filter = ['price']
    inlines = [ Ratesinlines]


       # return obj.Rates.opinion

    def average_rate(self, obj):

        ratings = Rates.objects.filter(clothing=obj)
        if ratings.exists():
            average_rate = sum([rating.rate for rating in ratings]) / len(ratings)
            return round(average_rate, 2)
        return "Brak ocen"


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ['name','rate','opinion','date_created']
    list_filter=['rate']

    def name(self,obj):
        return obj.clothing.name


