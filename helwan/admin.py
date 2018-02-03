from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import student,perc


class studentInline(admin.StackedInline):
    model = student
    can_delete = False
    verbose_name_plural = 'student'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (studentInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(perc)
