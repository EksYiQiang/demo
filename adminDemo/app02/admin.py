from django.contrib import admin

# Register your models here.


from app02.models import Food

admin.site.register(Food)

print("_registry2:-------->", admin.site._registry)

