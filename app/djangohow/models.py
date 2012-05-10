
from registration.signals import user_registered

def activate_user(sender, user, request, **kwargs):
    user.is_active = True
    user.save()

user_registered.connect(activate_user)
