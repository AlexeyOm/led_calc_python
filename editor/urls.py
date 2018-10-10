from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('editor/', views.editor_main, name='editor_main'),
    path('editor/<int:pk>/', views.cabinets, name='cabinets'),
    path('editor/cabinet/<int:pk>/', views.cabinet_editor, name='cabinet_editor'),
    path('editor/cabinet/new/', views.cabinet_add, name='cabinet_add'),
    path('editor/data/', views.get_data, name='get_data'),
    path('loginpage/', LoginView.as_view(template_name='admin/login.html', extra_context={'title': 'Login', 'site_title': 'My Site', 'site_header': 'My Site Login'}), name='login'),
]