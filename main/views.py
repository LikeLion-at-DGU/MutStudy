from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def worksingle(request):
    return render(request, 'main/work-single.html')

def work(request):
    return render(request, 'main/work.html')
