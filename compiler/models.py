from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = self.code.lower()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Programming Language"
        verbose_name_plural = "Programming Languages"

        ordering = ['name']
        unique_together = ['name', 'code']

        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return self.name
    
    
