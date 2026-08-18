from django.db import models
from django.utils.text import slugify


# Create your models here.
class Service(models.Model):

    title = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=250,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fa-solid fa-code"
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
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Web Development, Software, Cloud"
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    url = models.URLField(
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)

    position = models.CharField(
        max_length=150,
        blank=True,
        help_text="Example: CEO, ABC Company"
    )

    message = models.TextField()

    photo = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    rating = models.PositiveSmallIntegerField(
        choices=[
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
        default=5
    )

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.name
class AboutPage(models.Model):
    title = models.CharField(
        max_length=200,
        default="Building Digital Solutions That Move Businesses Forward"
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField()

    mission = models.TextField()

    vision = models.TextField()

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    years_experience = models.PositiveIntegerField(
        default=0
    )

    projects_completed = models.PositiveIntegerField(
        default=0
    )

    clients_served = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return self.title


class AboutValue(models.Model):
    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fa-solid fa-lightbulb"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "About Value"
        verbose_name_plural = "About Values"

    def __str__(self):
        return self.title