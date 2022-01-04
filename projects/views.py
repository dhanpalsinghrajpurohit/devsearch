from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
from django.http import HttpResponse,request

projectsList = [
        {
            'id':'1',
            'title':'Ecommerce website',
            'description':'Fully function ecommerce website'
        },
        {
            'id': '2',
            'title': 'Portfolio website',
            'description': 'This was a project where i built out my portfolio.'
        },
        {
            'id': '3',
            'title': 'Ecommerce website',
            'description': 'Fully function ecommerce website'
        }
    ]
def project(request):
    projects = Project.objects.all()
    msg = "Hello, You are on the project page."
    number = 5
    context = {'projects' :projects}
    return render(request, 'projects/projects.html', context)


def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)

    print(projectObj.featured_image)
    tags = projectObj.tags.all()
    print('projectObj', projectObj)
    return render(request,'projects/single_project.html',{'projects':projectObj,'tags':tags})


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


def updateproject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

def deleteproject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html',context)