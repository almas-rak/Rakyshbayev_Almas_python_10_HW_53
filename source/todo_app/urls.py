from django.urls import path

from todo_app.views.base import index_view

urlpatterns = [
    path('', index_view, name='home')
]