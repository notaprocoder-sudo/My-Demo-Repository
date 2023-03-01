from . import views
from django.urls import path, include
app_name = 'todoapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('cbvhome/', views.tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.taskdeleteview.as_view(), name='cbvdelete'),
]