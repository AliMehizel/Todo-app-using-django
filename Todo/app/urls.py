from django.urls import path   
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.LoginUser, name='login'),
    path('signup/', views.SignupUser, name='signup'),
    path('note/', views.ListNote, name='note'),
    path('createnote/', views.CreateNote, name='createnote'),
    path('deletenote/<int:pk>', views.DeleteNote, name='deletenote'),
    path('updatenote/<int:pk>', views.UpdateNote, name='updatenote'),
    path('updatenote/updated/<int:pk>', views.Updated, name='updated'),
]
