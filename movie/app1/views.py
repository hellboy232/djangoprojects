from django.shortcuts import render, redirect

from app1.forms import Movieform

from app1.models import Moviedetail


# Create your views here.

def movielist(request):
    movies = Moviedetail.objects.all()
    context = {'movies': movies}
    return render(request, 'movielist.html', context)

def addmovie(request):
    if request.method=='POST': #after submission
        form_instance=Movieform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            movies=Moviedetail.objects.all()
            context={'movies':movies}
            return render(request,'addmovie.html',context)

    if request.method=='GET':
        form_instance=Movieform()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)

def moviedetails(request,i):
    if request.method=='GET':
        m=Moviedetail.objects.get(id=i)
        return render(request,'moviedetails.html',{'movies':m})

def update(request,i):
    if request.method=="POST":
        m=Moviedetail.objects.get(id=i)
        f=Movieform(request.POST,request.FILES,instance=m)
        if f.is_valid():
            f.save()
            return redirect('app1:movielist')

    if request.method=="GET":
        m=Moviedetail.objects.get(id=i)
        f=Movieform(instance=m)
        context={'form':f}
        return render(request,'update.html',context)

def delete(request,i):
    m=Moviedetail.objects.get(id=i)
    m.delete()
    return redirect('app1:movielist')







