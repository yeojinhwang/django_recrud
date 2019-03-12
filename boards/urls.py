from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'), # boards:index
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    # path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]