from django.urls import path

from todo_app.views.base import index_view
from todo_app.views.todo_detail_view import detail_view

urlpatterns = [
    path('', index_view, name='home'),
    path('todo/<int:pk>', detail_view, name='todo_detail')
]
