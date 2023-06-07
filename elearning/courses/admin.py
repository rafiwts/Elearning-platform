from django.contrib import admin
from .models import Subject, Module, Course


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display: list = ['title', 'slug']
    prepopulated_fields: dict = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display: list = ['title', 'subject', 'created']
    list_filter: list = ['created', 'subject']
    search_fields: list = ['title', 'overview']
    prepopulated_fields: dict = {'slug': ('title',)}
    inline = [ModuleInline]