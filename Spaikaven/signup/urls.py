from django.conf.urls import url
from . import views

app_name = 'signup'

urlpatterns = [
	url(r'^$', views.signup_view, name='signup'),
     
]
