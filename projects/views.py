from django.shortcuts import render, redirect
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProject,paginateProject
from django.contrib import messages
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
# @login_required(login_url='login')
# def projects(request):
#     projects, search_query = searchProject(request)
#     custom_range, projects = paginateProject(request, projects, 3)
#     context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
#     return render(request, 'projects/projects.html', context)


def project(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginateProject(request, projects, 3)
    context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


@login_required(login_url='login')
def single_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        messages.success(request, "your review is successfully submitted.")
        return redirect('project', pk=projectObj.id)
    return render(request, 'projects/single_project.html', {'projects': projectObj, 'tags': tags,'form': form})


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    print(profile)
    form = ProjectForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def updateproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def deleteproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html',context)