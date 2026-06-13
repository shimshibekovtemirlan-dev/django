from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from school.views import RegisterView, TaskListCreateView,TaskDetailView
from school.views import UserProfileView




urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/schema/',SpectacularAPIView.as_view(),name='shame'),
    path('swagger/',SpectacularSwaggerView.as_view(url_name='shame'),name='swagger-ui'),

    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/task/', TaskListCreateView.as_view(), name='task_list_create'),
    path('api/task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),

]