from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . form import AddForm
from . models import Addpost

def homepage(request):
    query=Addpost.objects.all()
    cont={
        'q' :query
    }
    return render(request,'index.html',cont)

def addevent(request):
    if request.method == 'POST':
        f=AddForm(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return redirect('home')
    a=AddForm(label_suffix='')
    context={
        'form':a
    }
    return render(request,'addevent.html',context)


def change(request ,id ):
    todo = Addpost.objects.get(pk =id)
    rev=todo.is_liked
    if rev==True:
        rev=False
    else:
        rev=True
    todo.is_liked=rev
    todo.save()
    return redirect('home')