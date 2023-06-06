from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# projectsLists = [
#    { 'id' : '1',
#     'title' : 'Ecommerce Website',
#     'description' : 'Fully functional ecommerce website',
#     'topRated': True
#    },
#    {
#        'id' : '2',
#        'title' : 'Portfolio Website',
#        'description' : ' a personal website to write articles and display work',
#         'topRated': False
#    },
#    {
#        'id' : '3',
#        'title' : 'Social Network',
#        'description' : 'an open source project built by the community',
#         'topRated': True
#    }
# ]

def projects(request):
    # name = 'zebdiel s.'
    # gender = 'male'
    # age = 14
    # context = {'name':name, 'gender':gender, 'age':age}
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    # reviews = projectObj.reviews.all()
    context ={'project': projectObj}
    return render(request,'projects/single-projects.html', context)

def createProject(request):
    form = ProjectForm()

    # **** method to create a model form ***

    # if request.method == 'POST':
    #     print('FORM DATA:', request.POST)
    #     title = request.POST['title']

    #     Project.objects.create(
    #         title=title,
    #     )
    # this is the ideal way to do this then import redirect in views.py to send the user back to the homepage

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project-form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = { 'form':form}
    return render(request, 'projects/project-form.html', context)
    
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete.html', {'object':project})