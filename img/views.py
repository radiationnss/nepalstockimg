from django.shortcuts import render

def home_page(request):
    template = 'home_page.html'
    return render(request, template)

