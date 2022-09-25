from django.contrib import admin

# Register your models here.
from .models import Grade, LearningArea, Resource

admin.site.register(Grade)
admin.site.register(LearningArea)
admin.site.register(Resource)