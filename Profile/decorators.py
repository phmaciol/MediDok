from django.http import HttpResponse
from django.shortcuts import redirect

def unauth_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home_user')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('Nie masz dostępu do tej strony')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'Custom':
			return redirect('home_user')

		if group == 'personel':
			return redirect('home_per')

		if group == 'lekarz':
			return redirect('home_lek')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function