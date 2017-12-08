from django.db                  import models
from django.contrib.auth.models import User
from django.db.models.signals   import post_save
from django.dispatch            import receiver
from django.conf                import settings


#Profile model called by get_profile()

class Profile(models.Model):
    print("printed from models.py")
    #user = models.ForeignKey(User, unique=True)
    user = models.OneToOneField(User)                    #, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, default="", blank=True)

    #user = models.OneToOneField("auth.User")
    #color = models.CharField(max_length=10, default="", blank=True)

#    def __unicode__(self):
#        return u'Profile of user: %s' % self.user.username

#User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#create the profile automatically when a new user is "saved"
post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)   #User)

#def user_post_save(sender, instance, created, **kwargs):
     #Create a user profile when a new user account is created
#    if created == True:
#        p = UserProfile()
#        p.user = instance
#        p.save()

#post_save.connect(user_post_save, sender=User)