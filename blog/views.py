from django.shortcuts import render, get_object_or_404, redirect
from .models import blog #db 불러오기
from list.models import list
from django.utils import timezone
from .forms import BlogForm, listForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = blog.objects.order_by('-pub_date') #최신글 순서
    lists = list.objects.all()
    return render(request, "home.html", {'blogs': blogs, 'lists':lists} )

def detail(request, blog_id):
    Blog = get_object_or_404(blog, pk = blog_id) #2nd param = primary key. db상 row 식별자
    return render(request, "detail.html", {"blog":Blog})

def new(request):
    form = BlogForm()
    lat = request.POST['lat']
    lng = request.POST['lng']
    category= request.POST.get('category')
    return render(request, "new.html",{'form':form, 'lat':lat, 'lng':lng, 'category':category})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.writer = request.user.username
        print(new_blog.writer)
        print(request.POST.get('category'))
        new_blog.category = request.POST['category']
        new_blog.lat = request.POST['lat']
        new_blog.lng = request.POST['lng']
        new_blog.save()
        blogs = blog.objects.order_by('-pub_date')
        lists = list.objects.get(name = new_blog.category)
        return render(request, 'myMap.html', {'blogs': blogs, 'list':lists})
    return redirect('create')

def edit(request, id):
    edit_blog = blog.objects.get(id = id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id):
    update_blog = blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']    
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    Category = update_blog.category
    update_blog.save()
    return redirect('myMap', Category)

def delete(request, id):
    delete_blog = blog.objects.get(id = id)
    delete_blog.delete()
    Category = delete_blog.category
    return redirect('myMap', Category)

def myMap(request, Category):
    blogs = blog.objects.order_by('-pub_date')
    lists = list.objects.get(name = Category)   
    return render(request, 'myMap.html', {'blogs': blogs, 'list':lists})

def newList(request):
    if request.method == "GET":
        Category = request.GET.get('mapList')
        if(Category == 'add'):
            form = listForm()
            return render(request, 'newList.html', {'form': form})
        return redirect('myMap', Category)
    if request.method == "POST":
        tempForm = listForm(request.POST, request.FILES)
        if tempForm.is_valid():
            new_list = tempForm.save(commit=False)
            new_list.author = request.user.username
            new_list.save()
            Category = request.POST['name']
            return redirect('myMap', Category)
        return render(request, 'newList.html', {'form': tempForm})
