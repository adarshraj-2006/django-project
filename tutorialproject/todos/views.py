from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import PersonForm,TodoForm
from .models import Todo


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
        form=PersonForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            job=form.cleaned_data['job']

            return HttpResponse(f'You posted name : {name},{age} and {job}')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def submit_example(request):
    return render(request,'todos/submit.html     ')   

def submit_django_form(request):
    form=PersonForm()
    return render(request,'todos/submit_django_form.html',{'form':form})
    
def template_view(request):
    context ={
        "name":"Heisenberg",
        "age":50,
        "skills":["Chemistry","Cooking","Money Laundering"],
        "job":"Teacher + Chemist",
    }
    return render(request, 'todos/template_demo.html',context)

def todos(request):
    if request.method == 'POST':
        todo =TodoForm(request.POST)

        if todo.is_valid():
            todo = todo.save()
            return HttpResponse('Todo successfully created !')
        else:
            return HttpResponse('Invalid data !')
    
    else:
        form =TodoForm()
        todos =Todo.objects.all()

        return render(request,'todos/todos.html',{'form': form,'todos':todos})
def person_details(request,person_id):
    person=person.objects.filter(id =person_id).first()
    return render('todos/person_details.html',{'person':person})