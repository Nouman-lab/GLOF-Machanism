from django.db import models
from django.core.validators import MinValueValidator


class Glacier(models.Model):
    RISK_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    name = models.CharField(max_length=200)
    volume = models.FloatField(validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='glacier_images/')
    description = models.TextField()
    event_type = models.CharField(max_length=100)
    outburst_mechanism = models.TextField()
    area_map = models.ImageField(upload_to='area_maps/')
    area_description = models.TextField()
    risk_level = models.CharField(max_length=20, choices=RISK_LEVELS)
    risk_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def risk_level_color(self):
        return {
            'low': 'success',
            'medium': 'warning',
            'high': 'danger',
            'critical': 'dark',
        }[self.risk_level]


    @property
    def risk_percentage(self):
        return {
            'low': 25,
            'medium': 50,
            'high': 75,
            'critical': 100,
        }[self.risk_level]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at'] 