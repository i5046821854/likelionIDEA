from django.contrib import admin
from .models import CustomUser
from blog.models import blog
from list.models import list

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(list)