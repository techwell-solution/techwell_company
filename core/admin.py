from django.contrib import admin
from .models import Service, Project, Testimonial, AboutPage, AboutValue

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_featured",
        "is_active",
        "order",
        "created_at",
    )

    list_filter = (
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "order",
        "-created_at",
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "is_featured",
        "is_active",
        "order",
        "created_at",
    )

    list_filter = (
        "is_featured",
        "is_active",
        "category",
    )

    search_fields = (
        "title",
        "description",
        "category",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "order",
        "-created_at",
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "position",
        "rating",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "rating",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "position",
        "message",
    )

    list_editable = (
        "is_featured",
        "is_active",
        "order",
    )

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "years_experience",
        "projects_completed",
        "clients_served",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )


@admin.register(AboutValue)
class AboutValueAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "order",
    )