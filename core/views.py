from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Testimonial, AboutPage, AboutValue
from projects.models import Project
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ContactMessageForm
from .email_utils import send_resend_email

# Create your views here.

def home(request):

    featured_services = Service.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by("order", "-created_at")[:3]
    featured_projects = Project.objects.filter(
        is_active=True,
        featured=True
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

def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            contact_message = form.save()

            # Details for the company
            service_name = (
                contact_message.service.title
                if contact_message.service
                else "Not specified"
            )

            company_email = f"""
                <h2>New Contact Message - TechWell Company</h2>

                <p><strong>Name:</strong> {contact_message.name}</p>
                <p><strong>Email:</strong> {contact_message.email}</p>
                <p><strong>Phone:</strong> {contact_message.phone or "Not provided"}</p>
                <p><strong>Subject:</strong> {contact_message.subject}</p>
                <p><strong>Service:</strong> {service_name}</p>

                <h3>Message</h3>
                <p>{contact_message.message}</p>
            """

            # Confirmation for the client
            client_email = f"""
                <h2>Thank you for contacting TechWell Company</h2>

                <p>Dear {contact_message.name},</p>

                <p>
                    Thank you for reaching out to TechWell Company.
                    We have received your message and will get back to you soon.
                </p>

                <p><strong>Subject:</strong> {contact_message.subject}</p>

                <p>
                    We appreciate your interest in our services.
                </p>

                <p>
                    Regards,<br>
                    <strong>TechWell Company</strong>
                </p>
            """

            try:
                # Send notification to TechWell
                send_resend_email(
                    "techsolution89@yahoo.com",
                    f"New Contact Message: {contact_message.subject}",
                    company_email,
                )

                # Send confirmation to client
                send_resend_email(
                    contact_message.email,
                    "We received your message - TechWell Company",
                    client_email,
                )

                messages.success(
                    request,
                    "Thank you for contacting TechWell. "
                    "Your message has been received."
                )

            except Exception as e:
                print(f"Email sending error: {e}")

                messages.warning(
                    request,
                    "Your message was received, but we could not send "
                    "the email confirmation. We will still get back to you."
                )

            return redirect("contact")

    else:
        form = ContactMessageForm()

    context = {"form": form}
    return render(request, "core/contact.html", context)