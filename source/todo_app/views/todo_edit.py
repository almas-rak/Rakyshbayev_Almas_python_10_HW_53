from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from todo_app.models import TODO


def todo_edit(request: WSGIRequest, pk):
    if request.method == "GET":
        todo = TODO.objects.get(pk=pk)
        context = {'todo': todo}
        return render(request, 'todo_edit.html', context=context)
    print(request.POST)
    print(pk)
    todo = TODO.objects.get(pk=pk)
    todo.title = request.POST.get('title')
    todo.description = request.POST.get('description')
    todo.status = request.POST.get('status')
    if request.POST.get('date_of_completion') == "":
        todo.date_of_completion = None
    else:
        todo.date_of_completion = request.POST.get('date_of_completion')
    todo.save()

    return redirect('todo_detail', pk)
