from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Solution, Project
from .forms import BookingForm
from core.email_utils import send_resend_email

# Create your views here.
def solutions(request):
    solutions = Solution.objects.filter(
        is_active=True
    )

    featured_solutions = solutions.filter(
        is_featured=True
    )

    context = {
        "solutions": solutions,
        "featured_solutions": featured_solutions,
    }

    return render(
        request,
        "projects/solutions.html",
        context
    )

def projects(request):
    project_list = Project.objects.filter(
        is_active=True
    ).order_by("-created_at")

    paginator = Paginator(project_list, 3)  

    page_number = request.GET.get("page")

    projects_page = paginator.get_page(page_number)

    context = {
        "projects": projects_page,
    }

    return render(request, "projects/projects.html", context)

def project_detail(request, slug):
    """
    Display details for a single project.
    """

    project = get_object_or_404(
        Project,
        slug=slug,
        is_active=True
    )

    context = {
        "project": project,
    }

    return render( request,  "projects/project_detail.html", context)

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            service_name = booking.service.title

            company_email = f"""
                <h2>New Service Booking - TechWell Company</h2>

                <p><strong>Name:</strong> {booking.name}</p>
                <p><strong>Email:</strong> {booking.email}</p>
                <p><strong>Phone:</strong> {booking.phone}</p>
                <p><strong>Service:</strong> {service_name}</p>
                <p><strong>Budget:</strong> {booking.get_budget_display()}</p>
                <p><strong>Preferred Date:</strong> {
                    booking.preferred_date or "Not specified"
                }</p>
                <p><strong>Priority:</strong> {booking.get_priority_display()}</p>
                <p><strong>Website:</strong> {
                    booking.website_url or "Not provided"
                }</p>

                <h3>Project Description</h3>
                <p>{booking.description}</p>

                <p>
                    <strong>Status:</strong>
                    {booking.get_status_display()}
                </p>
            """

            try:
                send_resend_email(
                    "techsolution89@yahoo.com",
                    f"New Service Booking: {service_name}",
                    company_email,
                )
            except Exception as e:
                print(f"Booking email error: {e}")

            return redirect(
                "projects:booking_success",
                booking_id=booking.id
            )

    else:
        form = BookingForm()

    context = {"form": form}
    return render(request, "projects/booking.html", context)

def booking_success(request, booking_id):

    return render(request, "projects/booking_success.html", {"booking_id": booking_id,})

def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(request,  "projects/project_detail.html", {"project": project,})