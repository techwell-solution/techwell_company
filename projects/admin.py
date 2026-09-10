from django.contrib import admin
from .models import Solution, Project, Booking
#Project

# Register your models here.
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "category",
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
        "client",
        "featured",
        "is_active",
        "order",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "is_active",
    )

    search_fields = (
        "title",
        "client",
        "technologies",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "featured",
        "is_active",
        "order",
    )

    ordering = (
        "order",
        "-created_at",
    )
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "service",
        "budget",
        "preferred_date",
        "priority",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "priority",
        "budget",
        "service",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "description",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Client Information",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                )
            },
        ),

        (
            "Project Information",
            {
                "fields": (
                    "service",
                    "description",
                    "website_url",
                    "budget",
                    "preferred_date",
                    "priority",
                )
            },
        ),

        (
            "Booking Management",
            {
                "fields": (
                    "status",
                    "admin_notes",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )