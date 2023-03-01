from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

class tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task','prio','date')

    def get_success_url(self):
        return reverse('todoapp:cbvdetail', kwargs={'pk': self.object.id})

class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')


def home(request):
    tasklist = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('taskname','')
        priority = request.POST.get('taskprio','')
        date = request.POST.get('taskdate','')
        add_task = Task(task=name,prio=priority, date=date)
        add_task.save()
        return redirect('/')

    return render(request,'home.html',{'task':tasklist})

def delete(request, id):
    deltask = Task.objects.get(id=id)
    if request.method == 'POST':
        deltask.delete()
        return redirect('/')
    return render(request, 'delete.html',{'tsk':deltask})

def edit(request, id):
    tosk = Task.objects.get(id=id)
    fo = todoform(request.POST or None, instance=tosk)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': fo, 'task':tosk})

