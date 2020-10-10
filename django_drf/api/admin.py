from django.contrib import admin

# Register your models here.

from .models import Task, Article

admin.site.register([Task, Article])