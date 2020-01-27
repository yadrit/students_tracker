from django.contrib import admin
from students.models import Student, Group
from teachers.models import Teacher
from students.forms import StudentAdminForm


class GroupInline(admin.StackedInline):
    model = Group


class StudentInline(admin.TabularInline):
    model = Student
    readonly_fields = ('email', )
    show_change_link = True


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', )
    list_display = ('id', 'first_name', 'last_name', 'email', 'telephone', 'group')
    list_select_related = ('group', )
    list_per_page = 10
    inlines = [GroupInline, ]
    form = StudentAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone', )
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False

# Registering of StudentAdmin class


admin.site.register(Student, StudentAdmin)


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('group_code', )
    list_display = ('id', 'group_code', 'num_of_students', 'senior', 'curator')
    list_select_related = ('senior', )
    list_per_page = 10
    inlines = [StudentInline]

# Registering of GroupAdmin class


admin.site.register(Group, GroupAdmin)


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('email', )
    list_display = ('id', 'degree', 'first_name', 'last_name', 'email', 'telephone')
    list_per_page = 10

# Registering of TeacherAdmin class


admin.site.register(Teacher, TeacherAdmin)
