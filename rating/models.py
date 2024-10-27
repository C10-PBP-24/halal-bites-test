import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from food.models import Food
from django.conf import settings

class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=uuid.uuid4)  # Provide a default UUID value
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food.name} - {self.rating} by {self.user.username}"