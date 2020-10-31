from django.contrib import admin
from .models import user, Business, neighbourhood

# Register your models here.

admin.site.register(user)
admin.site.register(neighbourhood)
admin.site.register(Business)
