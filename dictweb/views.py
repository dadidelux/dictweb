from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'main/index.html'
    context = {
            # dictionary
    }
    return render(request, template, context)

# Create your views here.
def about(request):
    template = 'main/secondary/about.html'
    context = {
            # dictionary
    }
    return render(request, template, context)