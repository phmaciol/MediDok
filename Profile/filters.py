import django_filters
from  Profile.models import *
from django.contrib.auth.models import User, Group

class Personal_filters(django_filters.FilterSet):

    class Meta:
        model = Personal_med
        fields = ['last_name', 'first_name', 'pesel']
class User_filters(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']