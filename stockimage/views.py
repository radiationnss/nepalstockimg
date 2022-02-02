from .forms import AddImageForm
from django.shortcuts import render, redirect

def add_image_view(request):
    if request.method == "POST":
        form = AddImageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home/', slug=post.slug)
    else:
        form = AddImageForm()
    template = 'stockimage/addnew.html'
    context = {'form':form}
    return render(request, template, context)
