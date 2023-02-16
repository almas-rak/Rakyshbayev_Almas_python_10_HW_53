from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from todo_app.models import TODO


def detail_view(request: WSGIRequest, pk):
    todo = get_object_or_404(TODO, pk=pk)
    return render(request, 'detail_view_todo.html', context={
        'todo': todo
    })
