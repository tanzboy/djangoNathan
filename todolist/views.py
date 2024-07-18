from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import reverse
from .models import Todo
from django.shortcuts import get_object_or_404, redirect
#create your views here.

def index(request):
    all_todos = Todo.objects.all()
    context = dict(
        todos = all_todos
    )
    return render(request, 'todolist/index.html', context)
def add(request):
    new_todo = request.POST['todo']
    todo = Todo(text=new_todo)
    todo.save()

    #mau return ke index dengan cara memanggil url jangan fuctionnya
    #cara memanggil url berdasarkan nama dengan reverse
    return HttpResponseRedirect(reverse('todo-index'))

def update(request, todo_id):
    #merubah status ya bukan teks
    todo = Todo.objects.get(id=todo_id)
    todo.status = not todo.status# membolak balikan status tanpa if else
    todo.save()

    return HttpResponseRedirect(reverse('todo-index'))


def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo-index'))