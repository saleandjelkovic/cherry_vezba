from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user_login'

urlpatterns = [
	path('login/', LoginView.as_view(template_name='user_login/login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
]
