from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'), # boards:index
    path('new/', views.new, name='new'),
    path('<int:board_pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('edit/<int:board_pk>/', views.edit, name='edit'),
    # path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:board_pk>', views.delete, name='delete'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]