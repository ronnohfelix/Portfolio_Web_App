from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def contact(request):
    
    return render(request, 'contact.html')

def projects(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'project.html', {'project': project})