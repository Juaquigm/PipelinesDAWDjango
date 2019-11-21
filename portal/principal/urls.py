from django.urls import path, include
from .views import *

urlpatterns = [
    # Se asocian las diferentes url a las vistas
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('registro/', registro_view, name='registro_view'),
    path('', index, name='index'),
]
