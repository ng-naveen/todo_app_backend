from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .serializers import UserSerializer, TaskSerializer
from rest_framework import authentication, permissions
from .models import Task
from django.http import JsonResponse


class UserView(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    authentication_classes =[]
    permission_classes = [permissions.AllowAny]



class TaskView(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

    def create(self, request, *args, **kwargs):
        if request.data.get('status') == '':
            request.data['status'] = 'pending'

        if request.data.get('priority') == '':
            request.data['priority'] = 'low'

        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        if request.data.get('status') == '':
            request.data['status'] = 'pending'

        if request.data.get('priority') == '':
            request.data['priority'] = 'low'
        return super().update(request, *args, **kwargs)
    

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

def status_choices(request):
    return JsonResponse(dict(Task.STATUS_CHOICES))


def priority_choices(request):
    return JsonResponse(dict(Task.PRIORITY_CHOICES))
