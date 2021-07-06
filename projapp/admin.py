from django.contrib import admin
from .models import Details,Enrolled
# Register your models here.
admin.site.register(Details)
admin.site.register(Enrolled)

class DetailsAdmin(admin.ModelAdmin):
    list_display=['number','dept','course_name','duration','seats_available','fee']

 
class EnrolledAdmin(admin.ModelAdmin):
    list_display=['sno','user','c_name','department']

