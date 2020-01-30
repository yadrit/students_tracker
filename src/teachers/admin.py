from django.contrib import admin
from teachers.models import Teacher
from teachers.forms import TeacherAdminForm


# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', )
    list_display = ('id', 'degree', 'first_name', 'last_name', 'email', 'telephone')
    list_per_page = 10
    form = TeacherAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False

# Registering of TeacherAdmin class
admin.site.register(Teacher, TeacherAdmin)
