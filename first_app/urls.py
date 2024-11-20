from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.django_form,name='django-form'),
    path('model/',views.viewmodel,name='viewmodel')
]
