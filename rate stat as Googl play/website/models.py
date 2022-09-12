
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class RateStars(models.Model):
    img = models.ImageField(upload_to="images/")
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(f"id = {self.pk} score = {self.score}")