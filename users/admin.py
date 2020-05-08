from django.contrib import admin

# Register your models here
from .models import Cadet
from .models import Company

admin.site.register(Cadet)
admin.site.register(Company)
