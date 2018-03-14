from django.shortcuts import render
from django.contrib.auth.models import User, Grup
from rest_framework import viewsets
from tutoral.quickstart.serializers import UserSerializer, GroupSerializer 


class UserViewSet(viewsets.ModelViewSet):
	"""API endpoint that allows users to be viewed or edited."""

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
