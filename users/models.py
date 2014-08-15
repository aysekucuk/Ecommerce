from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class Accounts(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    name = models.CharField(max_length = 200, verbose_name = ('name'))
    surname = models.CharField(max_length = 200 , verbose_name = ('surname'))
    email = models.EmailField(max_length = 500, verbose_name = ('email'))
    join_date = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = ('join date'))
    slug = models.SlugField(max_length = 250, blank = True, null = True)

    def __init__(self):
    	return self.name

	def save(self):
		self.slug = slugify(self.user.username.upper())
		super(Accounts, self).save()