from django.contrib import admin

# Register your models here.
from deepseaweb import models as deepseaweb_models
from django.db.models.base import ModelBase

# Very hacky! (stolen from https://www.protechtraining.com/blog/post/477)
for name, var in deepseaweb_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)
