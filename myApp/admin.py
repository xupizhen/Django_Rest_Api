from django.contrib import admin

# Register your models here.

from .models import Grades,Students

# Register
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDetele']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    # 添加/修改页面
    # fields = ['gboynum', 'isDetele', 'gname', 'gdate', 'ggirlnum']
    fieldsets = [
        ("num", {"fields":['ggirlnum', 'gboynum']}),
        ("base", {"fields":['gname', 'gdate','isDetele']})
    ]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # gender.short_description = "性别"
    list_display = ['pk', 'sname', gender, 'sage', 'scontend', 'isDetele', 'sgrade']
    list_filter = ['sgrade']
    list_per_page = 5
admin.site.register(Grades, GradesAdmin)
# admin.site.register(Students, StudentsAdmin)
