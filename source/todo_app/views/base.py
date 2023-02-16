from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from todo_app.models import TODO


def index_view(request: WSGIRequest):
    todos = TODO.objects.all()
    context = {
        'todo': todos
    }

    return render(request, 'index.html', context=context)
