from django.contrib import admin

# Register your models here.

from .models import registration_detail

admin.site.register(registration_detail)


from .models import Questions
admin.site.register(Questions)
