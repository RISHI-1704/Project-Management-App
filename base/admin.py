from django.contrib import admin
from .models import UserProfile,Project,Tasks


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Tasks)