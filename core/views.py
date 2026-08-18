from django.shortcuts import render, get_object_or_404
from .models import Service, Project, Testimonial, AboutPage, AboutValue
from django.core.paginator import Paginator

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
    about_page = AboutPage.objects.filter(
        is_active=True
    ).first()

    values = AboutValue.objects.filter(
        is_active=True
    )

    context = {
        "about_page": about_page,
        "values": values,
    }
    return render(request, "core/about.html", context )


def services(request):

    service_list = Service.objects.filter(
        is_active=True
    ).order_by("order")

    paginator = Paginator(service_list, 3)  
    page_number = request.GET.get("page")

    services = paginator.get_page(page_number)

    context = {
        "services": services,
    }

    return render(
        request,
        "core/services.html",
        context
    )

def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    context = {"service": service,}

    return render(request,  "core/service_detail.html", context)