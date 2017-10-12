from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,'firstapp/one.html')

def other(request):
    return render(request,'firstapp/other.html')

def relative(request):
    return render(request,'firstapp/relative.html',{'relative_dict':"This is a filter message"})
