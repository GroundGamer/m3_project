from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# from app.models import ContentType_model, Permission_model

admin.site.register(ContentType)
admin.site.register(Permission)
