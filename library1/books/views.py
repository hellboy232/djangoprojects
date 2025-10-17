from django.shortcuts import render, redirect

from books.form import Books
from books.models import Book
from django.db.models import Q

#function based
# Create your views here.
# def home(request):
#     return render(request,'home.html')

#class based
from django.views import View
from pyexpat.errors import messages


class Home(View):
    def get(self,request):
        return render(request,'home.html')

    # def addbooks(request):
    #     if request.method=='POST':
    #         form_instance=Books(request.POST,request.FILES)
    #         if form_instance.is_valid():
    #             form_instance.save()
    #             return redirect('books:viewbooks')

            # data=form_instance.cleaned_data
            # t=data['title']
            # a=data['author']
            # pg=data['page']
            # p=data['price']
            # l=data['language']
            # b=Book.objects.create(title=t,author=a,pages=pg,price=p,language=l)
            # b.save()
            # context={'title':t,'author':a,'page':pg,'price':p,'language':l}

    # if request.method == 'GET':
    #     form_instance = Books()
    #     context={'form':form_instance}
    #     return render(request, 'addbooks.html',context)

class Addbooks(View):
    def post(self, request):
        form_instance = Books(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')
    def get(self,request):
        form_instance=Books()
        context={'form':form_instance}
        return render(request,'addbooks.html',context)



class Viewbooks(View):
    def get(self,request):
        b=Book.objects.all() # to read records from table
        context={'book':b}
        return render(request,'viewbooks.html',context)




class Bookdetails(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        context={'books':b}
        return render(request, 'bookdetails.html',context)

class Editbooks(View):
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=Books(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:viewbooks')

    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=Books(instance=b)
        context={"form":form_instance}
        return render(request, 'editbook.html',context)


class Deletebooks(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect("books:viewbooks")

class Search(View):
    def get(self,request):
        query=request.GET['q']
        # print(query)
        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            context = {'book': b}
            return render(request,'search.html',context)






