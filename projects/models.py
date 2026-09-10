from django.db import models
from django.utils.text import slugify


# Create your models here.
class Solution(models.Model):

    title = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    short_description = models.CharField(
        max_length=250
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fa-solid fa-globe"
    )

    image = models.ImageField(
        upload_to="solutions/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web", "Web Development"),
        ("software", "Software Development"),
        ("mobile", "Mobile Development"),
        ("cloud", "Cloud Solutions"),
        ("digital", "Digital Solutions"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    short_description = models.CharField(
        max_length=250
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    technologies = models.CharField(
        max_length=300,
        blank=True,
        help_text="Example: Django, Python, JavaScript, React"
    )

    client = models.CharField(
        max_length=150,
        blank=True
    )

    project_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

class Booking(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("reviewing", "Under Review"),
        ("confirmed", "Confirmed"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    PRIORITY_CHOICES = [
        ("normal", "Normal"),
        ("urgent", "Urgent"),
    ]

    BUDGET_CHOICES = [
        ("under_20k", "Under KSh 20,000"),
        ("20k_50k", "KSh 20,000 – 50,000"),
        ("50k_100k", "KSh 50,000 – 100,000"),
        ("100k_250k", "KSh 100,000 – 250,000"),
        ("over_250k", "KSh 250,000+"),
        ("not_sure", "Not sure / Need consultation"),
    ]

    # Client information
    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=30)

    # Service requested
    service = models.ForeignKey(
        "core.Service",
        on_delete=models.PROTECT,
        related_name="bookings"
    )

    # Project information
    description = models.TextField()

    website_url = models.URLField(
        blank=True,
        null=True
    )

    budget = models.CharField(
        max_length=30,
        choices=BUDGET_CHOICES,
        default="not_sure"
    )

    preferred_date = models.DateField(
        blank=True,
        null=True
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="normal"
    )

    # Booking management
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    admin_notes = models.TextField(
        blank=True
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.name} - {self.service.title}"