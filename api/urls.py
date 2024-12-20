from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register('user', views.UserView, basename='user')
router.register('task', views.TaskView, basename='task')

urlpatterns = [
    path('token/', ObtainAuthToken.as_view(), name='token'),
    path('status-choices/', views.status_choices, name='get-status'),
    path('priority-choices/', views.priority_choices, name='get-priority'),
    path('', include(router.urls)),
]
