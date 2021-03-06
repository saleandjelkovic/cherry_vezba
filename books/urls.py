from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:book_id>/', views.details_books, name='details_books'),
    path('<int:book_id>/edit/', views.edit_books, name='edit_books'),
    path('enter_new_book', views.enter_new_book, name="enter_new_book"),
    path('ajax/load-emails', views.load_emails, name='ajax_load_emails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
