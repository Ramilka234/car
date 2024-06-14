from django.contrib import admin
from .models import Car, Inspection,ServiceRecord, Article

admin.site.register(Car)
admin.site.register(Inspection)
admin.site.register(ServiceRecord)
admin.site.register(Article)
