from django.urls import path
from . import views

urlpatterns = [

    path('hello',views.hello_world,name = 'hello+world'),
    path('',views.hello_python,name="hello python !"),
    path('htmlrender',views.hello_html_view,name="hello_html"),
    path('helloname/<str:name>',views.hello_name,name="hello+name"),
    path('add/<int:num1>/<int:num2>',views.add,name='add two numbers'),
    path('helloquery',views.hello_query,name='hello query'),
    path('special',views.special_view,name='special view '),
    path('postexample',views.post_example,name='post example'),
    path('submit',views.submit_example,name='submit example'),
    path('submitdjango',views.submit_django_form,name='submit django form'),
    path('templateview',views.template_view,name='template view'),
    path('todos',views.todos,name='todos'),
]