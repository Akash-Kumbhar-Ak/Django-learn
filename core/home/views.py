from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people=[
        {'name':'Abhishek','age':13,'city':'Delhi'},
            {'name':'Rahul','age':24,'city':'Mumbai'},
            {'name':'Aman','age':15,'city':'Pune'},
            {'name':'Ankit','age':26,'city':'Chennai'},
            {'name':'Anurag','age':17,'city':'Kolkata'}
    ]
    fruits=['apple','banana','mango','grapes']
    text="doloribus eligendi omnis aspernatur eius earum perferendis ea! Aspernatur ad aperiam quam, voluptas quia tenetur reiciendis velit repellendus cum ratione impedit magni vitae hic ab quisquam nemo ullam esse ipsa, perferendis voluptates est ut iusto! Non quas aspernatur pariatur accusamus! Ad corrupti similique cumque error, distinctio ipsum in odio cupiditate non aliquid optio libero, doloremque facilis, vitae odit officiis adipisci eos! Recusandae neque eius doloremque."
    return render(request,'index.html', context={'people':people,'text':text,'fruits':fruits})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def success_page(request):
    return HttpResponse("<h1>Hey i am django success page</h1>")