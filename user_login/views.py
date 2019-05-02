from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.urls import reverse


def signup(request):
	if (request.method == 'POST'):
		form = UserCreationForm(request.POST)
		if (form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('user_login:login'))
	else:
		form = UserCreationForm()

	token = {}
	token.update(csrf(request))
	token['form'] = form

	return render(request, 'user_login/signup.html', token)
