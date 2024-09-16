from django.urls import path
from . import auth_views, api_views
from django.contrib import admin

urlpatterns = [
    # Authentication-related paths
    path('api/signup/', auth_views.signup, name='signup'),
    path('api/login/', auth_views.login, name='login'),
    path('api/users/', auth_views.get_all_users, name='get_all_users'),
    path('api/admin/', auth_views.admin_view, name='admin_view'),
    path('api/editor/', auth_views.editor_view, name='editor_view'),

    # Other API paths
    path('api/candidat/all/', api_views.proxy_to_microservice_all, name='proxy_to_microservice_all'),
    path('api/candidat/<int:id>/', api_views.proxy_to_microservice_by_id, name='proxy_to_microservice_by_id'),
    path('api/another-endpoint/', api_views.some_other_api, name='some_other_api'),
    path('admin/', admin.site.urls),

]
