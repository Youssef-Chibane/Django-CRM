from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('create', views.create_record, name="create"),
    path('view/<int:pk>', views.view_record, name="view"),
    path('update/<int:pk>', views.update_record, name="update"),
    path('delete/<int:pk>', views.delete_record, name='delete'),
]
