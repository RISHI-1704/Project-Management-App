from django.urls import path
from .views import ProjectList,ProjectCreation,TaskCreation,ProjectDelete,TaskDelete,UserCreation,UserDeletion,ProjectDetails,EditTask,RemoveUser,AllUsers

urlpatterns = [
    path('',ProjectList.as_view(),name='projects'),
    path('create-project/',ProjectCreation.as_view(),name='create-project'),
    path('create-tasks/',TaskCreation.as_view(),name='create-tasks'),  
    path('delete-project/<int:pk>',ProjectDelete.as_view(),name='delete-project'),
    path('delete-task/<int:pk>',TaskDelete.as_view(),name='delete-task'),
    path('create-user',UserCreation.as_view(),name='create-user'),
    path('delete-user/<int:pk>',UserDeletion.as_view(),name='delete-user'),
    path('remove-user/<int:task_id>/<int:user_id>',RemoveUser.as_view(),name='remove-user'),
    path('project_details/<int:pk>',ProjectDetails.as_view(),name='project-details'),
    path('edit-task/<int:pk>',EditTask.as_view(),name='edit-task'),
    path('all-users',AllUsers.as_view(),name='all-users'),
]