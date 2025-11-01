from django.db import models
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL  # keep it flexible

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        # show username if full_name empty
        try:
            return self.full_name or self.user.username
        except Exception:
            return str(self.pk)

# Auto-create / save profile when user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # ensure profile exists and save
        UserProfile.objects.get_or_create(user=instance)
