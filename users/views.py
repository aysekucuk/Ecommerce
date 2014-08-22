from django.shortcuts import render
from userena.views import signin, signup as Signup, signout
from userena.decorators import secure_required

# Create your views here.
@secure_required
def login(request):

	# If user is authenticted, Redirect to home
	if request.user.is_authenticated():
		return redirect('home')

	return signin(request, template_name='auth/login.html')

@secure_required
def forgotpassword(request):
	return signout(request, next_page="/kullanici/giris")

@secure_required
def signup(request):
	# If user is authenticted, Redirect to home
	if request.user.is_authenticated():
		return redirect('home')

	return Signup(request, template_name='auth/signup.html', signup_form=SignupForm)

def logout(request):
	return signout(request, next_page="/")