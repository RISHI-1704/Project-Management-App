from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Project,Tasks,UserProfile
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView,DeleteView,DetailView
from .forms import TaskForm,ConfirmPass,TaskEdit,RemoveUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class UserCreation(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'base/user_create.html'
    success_url = reverse_lazy('projects')
    
class UserDeletion(View):
    template_name = 'base/user_delete.html'
    
    def get(self,request,pk):
        form = ConfirmPass()
        user = get_object_or_404(User,pk=pk)
        return render(request,self.template_name,{'form':form,'user_delete':user})
    
    def post(self,request,pk):
        form = ConfirmPass(request.POST)
        user = get_object_or_404(User,pk=pk)
        if form.is_valid():
            password = form.cleaned_data['password']
            if user.check_password(password):
                user.delete()
                return redirect('projects')
            else:
                form.add_error('password', 'Incorrect password.')
        return render(request, self.template_name, {'form': form, 'user_delete': user})    

class ProjectList(ListView):
    model = Project
    template_name = 'base/project_list.html'
    context_object_name = 'projects'
    

class ProjectCreation(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'base/project_create.html'
    success_url = reverse_lazy('projects')
    
class TaskCreation(CreateView):
    model = Tasks
    form_class= TaskForm
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('projects')
    
class ProjectDelete(DeleteView):
    model = Project
    template_name = 'base/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('projects')
    
class TaskDelete(DeleteView):
    model = Tasks
    template_name = 'base/delete_task.html'
    context_object_name = 'task'
    success_url = reverse_lazy('projects')
    
class ProjectDetails(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'base/project_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        tasks = project.tasks.all()
        context['tasks'] = tasks       
        return context
    
class EditTask(UpdateView):
    model = Tasks
    template_name = 'base/edit_task.html'
    form_class = TaskEdit
    context_object_name = 'task'
   
    def get_success_url(self):
        return reverse_lazy('project-details', kwargs = {'pk':self.object.project.id})
    
class RemoveUser(View):
    template_name ='base/remove_user.html'

    def get(self, request, task_id, user_id):
        task = get_object_or_404(Tasks, pk=task_id)
        user = get_object_or_404(User, pk=user_id)
        return render(request, self.template_name, {'task': task, 'user': user})

    def post(self, request, task_id, user_id):
        task = get_object_or_404(Tasks, pk=task_id)
        user = get_object_or_404(User, pk=user_id)
        task.users.remove(user)
        return redirect('project-details', pk=task.project.pk)
    
class AllUsers(ListView):
    model = UserProfile
    template_name = 'base/all_users.html'
    context_object_name = 'users'
    