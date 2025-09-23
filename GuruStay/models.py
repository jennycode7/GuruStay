from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

User = get_user_model()

class Profile():
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_host = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"
    


class Property(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property', blank=True, null=True)


    def __str__(self):
        return f"{self.title} | {self.location} | {self.price_per_night}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    Total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} | {self.property.title}"
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(default=5)  # scale 1–5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating}/5 by {self.user.username}"



class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    METHOD_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('transfer', 'Bank Transfer'),
        ('wallet', 'Wallet'),
        ('paypal', 'PayPal'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="payment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reference = models.CharField(max_length=100, unique=True)  # payment gateway ref
    transaction_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} → {self.booking.property.title} ({self.status})"