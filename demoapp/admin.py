from django.contrib import admin
from .models import Books, Contact, Register,Student

admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Books)
admin.site.register(Register)