from django.urls import path

from todo_app.views.base import index_view
from todo_app.views.todo_detail_view import detail_view
from todo_app.views.todo_edit import todo_edit

urlpatterns = [
    path('', index_view, name='home'),
    path('todo/<int:pk>', detail_view, name='todo_detail'),
    path('todo/edit/<int:pk>', todo_edit, name='edit_todo'),
]
