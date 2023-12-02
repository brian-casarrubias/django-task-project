from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
# Create your views here.



class TaskListView(LoginRequiredMixin,ListView):
    model = Task

    

    template_name = 'helloworld/index.html'
    #the variable is going to be sent to the template
    context_object_name = 'task'
    
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filter tasks based on the current user
            return Task.objects.filter(user=self.request.user).order_by('-date_posted')
        else:
            # User is not authenticated, return an empty queryset
            return Task.objects.none()
    

class TaskDetailView(LoginRequiredMixin,UserPassesTestMixin,  DetailView):
    model = Task

    def test_func(self):
        task = self.get_object()

        if self.request.user == task.user:
            return True
        else:
            return False




class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task


    fields = [
        'title', 
        'content',
        'completed',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Task Created!')
        return super().form_valid(form)
       



class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView ):
    model = Task

    fields = [
        'title',
        'content',
        'completed',
    ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Task Updated!')
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        else:
            return False
        

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task


    def test_func(self):
        task = self.get_object()

       

        if self.request.user == task.user:
            
            return True
        else:
            return False
       
       
        
  
    success_url = '/'