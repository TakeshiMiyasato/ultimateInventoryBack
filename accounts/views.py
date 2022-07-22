import json

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework import permissions, serializers, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        userne = User.objects.get(username=request.data['username'])
        login(request, user)
        updated = super(LoginAPI, self).post(request).data.copy()
        updated.update({'id': userne.pk, 'staff': userne.is_staff})
        return HttpResponse(
            json.dumps(updated)
            , content_type="application/json")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['post'], url_path='setRolAdmin', name='setRolAdmin')
    def setRolAdmin(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='setRolUser', name='setRolUser')
    def setRolUser(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='setPassword', name='setPassword')
    def setPassword(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.set_password(request.data['password'])
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
