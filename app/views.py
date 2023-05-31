from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Ashu','a':30}
    return render(request,'wish.html',context=d)
    return render(request,'wish.html',context=d)
def ifcondition(request):
    d={'a':30,'b':40}
    return render(request,'ifcondition.html',context=d)
def ifelif(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'ifelif.html',d)
def looping(request):
    d={'name':'ASHU'}
    return render(request,'looping.html',d)
