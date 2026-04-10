from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World !')
def hello_python(request):
    return HttpResponse("hello python !")
def hello_html_view(request):
    return render(request, 'todos/index.html')

def hello_name(request,name):
    return HttpResponse(f"hello {name} ... !")
def add(request,num1,num2):
    return HttpResponse(f"sum is {num1+num2}")

def hello_query(request):
    return HttpResponse(f"hello user , your query is {request.GET.get('query')}")

def special_view(request):
    return redirect(' hello_html  ')

def post_example(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        job=request.POST.get('job')

        return HttpResponse(f'You posted name : {name},{age} and {job}')
    else:
        return HttpResponseNotAllowed(['POST'])