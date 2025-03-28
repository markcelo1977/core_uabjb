from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'appfacultad/index.html')
# Compare this snippet from appfacultad/views.py: