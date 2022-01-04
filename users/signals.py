from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

# @receiver(post_delete,sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# @receiver(post_save,sender=Profile)
def profileUpdate(sender, instance, created, **kwargs):
    print('Profile Saved!')



post_save.connect(profileUpdate,sender=Profile)
post_delete.connect(deleteUser, sender=Profile)