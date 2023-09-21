from django.contrib import admin

# load the model first
from .models import Post

# Register your models here.
admin.site.register(Post)