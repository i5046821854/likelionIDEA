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
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = blog.objects.filter(writer = author)
        return render(request,'home.html', {'blogs': blogs, 'lists':lists} )
    paginator = Paginator(blogs,3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
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
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('home')

def myMap(request):
    if request.method == "POST":
        Category = request.POST.get('mapList')
        if(Category == 'add'):
            return redirect('newList')     
        blogs = blog.objects.order_by('-pub_date')
        lists = list.objects.get(name = Category)
    return render(request, 'myMap.html', {'blogs': blogs, 'list':lists})

def newList(request):
    if request.method == "POST":
        tempForm = listForm(request.POST, request.FILES)
        if tempForm.is_valid():
            new_list = tempForm.save(commit=False)
            new_list.author = request.user.username
            new_list.save()
            blogs = blog.objects.order_by('-pub_date')
            category = request.POST['name']
            lists = list.objects.get(name = category)
            print(request.user.username)
            print(lists.author)
            return render(request, 'myMap.html', {'blogs': blogs, 'list': lists})
        return render(request, 'newList.html', {'form': tempForm})
    else:     
        form = listForm()
        return render(request, 'newList.html', {'form': form})
