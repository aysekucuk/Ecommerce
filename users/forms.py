#-*- coding:utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm as signupForm, EditProfileForm as editProfileForm
from django import forms


CHOICES = (
	("None", _("-----")),
	(_("Male"), _("Male")), 
	(_("Female"), _("Female")))

class SignupForm(signupForm):
	firstname=forms.CharField(max_length=40)
	lastname=forms.CharField(max_length=40)
	gender = forms.ChoiceField(choices=CHOICES, label=_("Cinsiyet"))
	tos = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'required'}),
							 label=_(u'I have read and agree to the Terms of Service'),
							 error_messages={'required': _('You must agree to the terms to register.')})
	def __init__(self, *args, **kw):
		super(signupForm, self).__init__(*args, **kw)
		self.fields.keyOrder = [
			'firstname',
			'lastname',
			'username',
			'email',
			'password1',
			'password2',
			'gender',
			'tos',
				]

		self.fields['firstname'].label = u'Adınız'
		self.fields['lastname'].label = u'Soyadınız'
		self.fields['password1'].label = u'Parola (parolanız en az 5 karakter olmalıdır)'



	def clean_password1(self):
		password = self.cleaned_data.get('password1')
		# TODO Çevrilecek
		if len(password)<=4:
			raise forms.ValidationError('Parolanız 4 karakterden fazlasını içermelidir.')
		return self.data['password1']

	def save(self):
		user = super(SignupForm, self).save()
		user.profile.sex = self.cleaned_data.get('gender')
		user.profile.save()
		user.first_name = self.cleaned_data.get('firstname')
		user.last_name = self.cleaned_data.get('lastname')
		user.save()
		return user


class EditProfileForm(editProfileForm):
	class Meta:
		model = editProfileForm.Meta.model
		exclude = ['join_date', 'slug']+editProfileForm.Meta.exclude