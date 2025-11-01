from django.db import models
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    location = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    invited = models.ManyToManyField(User, related_name='invited_events', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_time.date()})"

    class Meta:
        ordering = ['-created_at']

class RSVP(models.Model):
    STATUS_GOING = 'going'
    STATUS_MAYBE = 'maybe'
    STATUS_NOT = 'not_going'
    STATUS_CHOICES = [
        (STATUS_GOING, 'Going'),
        (STATUS_MAYBE, 'Maybe'),
        (STATUS_NOT, 'Not Going'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rsvps')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.event.title} - {self.status}"

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.event.title} - {self.rating}"

