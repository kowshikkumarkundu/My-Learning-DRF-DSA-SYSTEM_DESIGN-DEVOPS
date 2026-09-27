from django.db import models


class Conversation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):

    ROLE_CHOICES = [
        ("user", "User"),
        ("assistant", "Assistant"),
    ]

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

class MenuItem(models.Model): 
    name = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    description = models.TextField(blank=True) 
    category = models.CharField(max_length=50) 
    is_available = models.BooleanField(default=True) 

    def __str__(self): 
        return self.name


class RestaurantInfo(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

