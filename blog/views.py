from django.shortcuts import render, get_object_or_404, redirect
from .models import blog #db 불러오기
from django.utils import timezone
from .forms import BlogForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = blog.objects.order_by('-pub_date') #최신글 순서
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = blog.objects.filter(writer = author)
        return render(request,'home.html', {'blogs': blogs})
    paginator = Paginator(blogs,3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, "home.html", {'blogs': blogs})

def detail(request, blog_id):
    Blog = get_object_or_404(blog, pk = blog_id) #2nd param = primary key. db상 row 식별자
    return render(request, "detail.html", {"blog":Blog})

def new(request):
    form = BlogForm()
    lat = request.POST['lat']
    lng = request.POST['lng']
    return render(request, "new.html",{'form':form, 'lat':lat, 'lng':lng})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.lat = request.POST['lat']
        new_blog.lng = request.POST['lng']
        new_blog.save()
        print(new_blog.lat)
        print(new_blog.lng)
        
        return redirect('detail', new_blog.id)
    return redirect('home')

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
