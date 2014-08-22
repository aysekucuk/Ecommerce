from django.conf.urls import patterns, url

import views
from forms import EditProfileForm

from django.contrib.auth import views as auth_views
from userena import views as userena_views
from userena import settings as userena_settings

urlpatterns = patterns('',

	# Signup, signin and signout
	url(r'^giris/$', views.login, name = u'login'),
	url(r'^kayit/$', views.signup, name = u'signup'),
	url(r'^cikis/$', views.logout, name = u'logout'),

	# Reset password
	url(r'^parola/sifirla/$',
		auth_views.password_reset,
		{'template_name': 'password_reset.html',
		'email_template_name': 'emails/password_reset_message.txt'},
		name='userena_password_reset'),
	
	url(r'^parola/sifirla/tamamlandi/$',
		auth_views.password_reset_done,
		{'template_name': 'password_reset_done.html'},
		name='userena_password_reset_done'),

	url(r'^parola/sifirla/dogrulama/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
		auth_views.password_reset_confirm,
		{'template_name': 'password_reset_confirm.html'},
		name='userena_password_reset_confirm'),
	
	url(r'^parola/sifirla/dogrulama/tamamlandi/$',
		auth_views.password_reset_complete,
		{'template_name': 'password_reset_complete.html'}),

	# Activate
	url(r'^aktif/(?P<activation_key>\w+)/$',
		userena_views.activate, {'template_name': 'activate_fail.html', 'success_url' : 'home'},
		name='userena_activate'),

	url(r'^(?P<username>[\.\w]+)/$',views.profile,name='userena_profile_edit'),

	# Edit profile
	url(r'^(?P<username>[\.\w]+)/duzenle/$',
		userena_views.profile_edit, {'template_name': 'profile/edit_profile.html', 'edit_profile_form': EditProfileForm },
		name='userena_profile_edit'),

	# Change password
	url(r'^(?P<username>[\.\w]+)/parola/$',
	   userena_views.password_change, {'template_name': 'profile/change_password.html' },
	   name='userena_password_change'),

	url(r'^(?P<username>[\.\w]+)/password/complete/$',
		userena_views.direct_to_user_template,
		{'template_name': 'profile/change_password_complete.html'},
		name='userena_password_change_complete'),
 
	# Change email and confirm it
	url(r'^(?P<username>[\.\w]+)/eposta/$',
	   userena_views.email_change, {'template_name': 'profile/change_email.html' },
	   name='userena_email_change'),

	url(r'^(?P<username>[\.\w]+)/eposta/tamamlandi/$',
	   userena_views.direct_to_user_template,
	   {'template_name': 'profile/email_change_complete.html'},
	   name='userena_email_change_complete'),

	url(r'^(?P<username>[\.\w]+)/eposta-dogrula/tamamlandi/$',
	   userena_views.direct_to_user_template,
	   {'template_name': 'profile/email_confirm_complete.html'},
	   name='userena_email_confirm_complete'),

	url(r'^eposta-dogrula/(?P<confirmation_key>\w+)/$',
	   userena_views.email_confirm,
	   name='userena_email_confirm'),

	# Signup
	url(r'^(?P<username>[\.\w]+)/kayit/tamamlandi/$',
		userena_views.direct_to_user_template,
		{'template_name': 'signup_complete.html',
		'extra_context': {'userena_activation_required': userena_settings.USERENA_ACTIVATION_REQUIRED,
						  'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS}},
		name='userena_signup_complete'),

	#not activated acoount
	url(r'^(?P<username>[\.\w]+)/disabled/$',
	   userena_views.direct_to_user_template,
	   {'template_name': 'not_activated_profile.html'},
	   name='userena_disabled'),

	# View profiles
	url(r'^(?P<username>(?!cikis|kayit|giris)[\.\w]+)/$', views.profile, name='userena_profile_detail'),
	url(r'^(?P<username>(?!cikis|kayit|giris)[\.\w]+)/(?P<type>evetler\b|\bhayirlar\b|\bfikirler\b|\bdogrutahminler\b|\byorumlar\b|\btakipettikleri\b|\btakipedenler)/$', views.profile, name='userena_profile_sections'),
)