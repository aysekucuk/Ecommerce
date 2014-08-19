from django.db import models
from django.utils.translation import ugettext as _


class Media(models.Model):
	name = models.CharField(max_length=100,blank=True, null=True, verbose_name=_('name'))
	image = models.ImageField(upload_to = "uploads", verbose_name = _('image'))

	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, verbose_name = _('name'))
	info = models.TextField(verbose_name = _('info'),blank=True,null=True)
	price = models.IntegerField(verbose_name = _('price'))
	quantity = models.IntegerField(default=0 ,verbose_name = _('quantity'))
	sold_count = models.IntegerField(default = 0, verbose_name = _('sold count'))
	photos = models.ManyToManyField(Media,verbose_name = _('photos'))

	def __unicode__(self):
		return self.name

	def save(self):
		self.slug = slugify(self.user.username.upper())
		super(Product, self).save()

