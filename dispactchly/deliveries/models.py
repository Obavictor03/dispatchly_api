from django.db import models

# Create your models here.
class Delivery(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    sender = models.ForeignKey('accounts.Sender', on_delete=models.CASCADE)
    rider = models.ForeignKey('accounts.Rider', on_delete=models.SET_NULL, null=True, blank=True)
    recipient_name = models.CharField(max_length=255)
    recipient_phone_number = models.CharField(max_length=20)
    pickup_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    pickup_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    dropoff_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    package_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery to {self.recipient_name} - Status: {self.get_status_display()}"
    
class Rating(models.Model):
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    rider = models.ForeignKey('accounts.Rider', on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.rider.user.name} - {self.rating}"