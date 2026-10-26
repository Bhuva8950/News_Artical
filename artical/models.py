
from django.db import models


class Article(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"
        
    url = models.URLField(max_length=2048, unique=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
    )
    company_name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

class ArticalData(models.Model):

    title = models.CharField(max_length=500)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="urls",
    )
    content = models.TextField()
    
    category = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )
    summary = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)


