from django.db import models


class Quote(models.Model):
    SERVICE_CHOICES = [
        ("kitchen", "Kitchen"),
        ("bathroom", "Bathroom"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="quotes_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} ({self.created_at:%Y-%m-%d})"
