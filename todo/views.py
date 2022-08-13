from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from todo.models import toDo
from todo.forms import toDoForm


def toDoHomeView(request):
    model = toDo 
    data = model.objects.all()
    return render(request, 'todo/todohome.html', {"data": data})

class createToDoFormView(CreateView):
    template_name = 'todo/createtodo.html'
    form_class = toDoForm
    
    def form_valid(self, form):
        if form.is_valid():
            print('save')
            instance = form.save(commit=False)
            instance.save()
        else:
            print('form error')
        return super(createToDoFormView, self).form_valid(form)
    
    success_url = reverse_lazy('todohome')

    
class deleteToDoFormView(DeleteView):
    model = toDo
    success_url = reverse_lazy('todohome')
