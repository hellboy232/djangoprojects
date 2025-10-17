from django.shortcuts import render, redirect

from books.form import Books
from books.models import Book


# Create your views here.
def home(request):
    return render(request,'home.html')

def addbooks(request):
    if request.method=='POST':
        form_instance=Books(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()

            # data=form_instance.cleaned_data
            # t=data['title']
            # a=data['author']
            # pg=data['page']
            # p=data['price']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,pages=pg,price=p,language=l)
            # b.save()
            # context={'title':t,'author':a,'page':pg,'price':p,'language':l}

            return redirect('books:viewbooks')
    if request.method == 'GET':
        form_instance = Books()
        context={'form':form_instance}
        return render(request, 'addbooks.html',context)


def viewbooks(request):
    b=Book.objects.all() # to read records from table
    context={'book':b}
    return render(request,'viewbooks.html',context)




def bookdetails(request,i):
    if request.method=="GET":
        b=Book.objects.get(id=i)
        context={'books':b}
        return render(request, 'bookdetails.html',context)

def editbooks(request,i):
    if request.method=="POST":
        b=Book.objects.get(id=i)
        form_instance=Books(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')

    if request.method == "GET":
        b=Book.objects.get(id=i)
        form_instance=Books(instance=b)
        context={"form":form_instance}
        return render(request, 'editbook.html',context)


def deletebooks(request,i):
    b=Book.objects.get(id=i)
    b.delete()
    return redirect("books:viewbooks")






