"""
This module contains database models for the furniture application.
"""
import os
from django.db import models
from django.contrib.auth.models import User


def upload_to(_instance, filename):
    """
    Handles file saving for the instance.
    """
    return os.path.join('uploads', filename)


class FurnitureItem(models.Model):
    """
    Represents a furniture item listed for sale or rent on the platform.
    """
    #seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    title = models.CharField(max_length=255)
    condition = models.CharField(max_length=255, default="Good")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_for_rent = models.BooleanField(default="Not Available For Rent")
    available_for_sale = models.BooleanField(default="Available For Sale")
    image = models.ImageField(upload_to='furniture/', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        """
        Returns the string representation of the furniture item.
        """
        return self.title # Assuming 'nmae' is a CharField

    def is_available(self):
        """
        Calculates and returns the quantity for the furniture item.
        """
        return self.quantity > 0
