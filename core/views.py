from django.shortcuts import render
from .models import Service, Project, Testimonial

# Create your views here.

def home(request):

    featured_services = Service.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by("order", "-created_at")[:3]
    featured_projects = Project.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by("order", "-created_at")[:6]
    testimonials = Testimonial.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by("order", "-created_at")


    context = {
        "featured_services": featured_services,
        "featured_projects": featured_projects,
        "testimonials": testimonials,
    }

    return render(request, "core/home.html", context )

def about(request):
    return render(request,"core/about.html" )