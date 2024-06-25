from django.contrib import admin
from .models import Product,Person,Student
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','address']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no','person']
admin.site.register(Person,PersonAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Student,StudentAdmin)
