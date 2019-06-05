from django.shortcuts import render, redirect, get_object_or_404 #없으면 404 에러를 띄워주겠다
from .models import Post, Comment
import pdb

# Create your views here.
def list(request):
    if request.method == "POST":
        name = request.POST.get('name')

    if 'name' in request.session:
        name = request.session['name']
        
    posts = Post.objects.all().order_by('-id')
    
    return render(request, 'pages/list.html', {'name': name, 'posts': posts})


def write_post(request):
    
    return render(request, 'pages/write.html')


def write_success(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        content = request.POST.get('content')
        image = request.FILES.get('file')
        
        post = Post(password=password, content=content, img=image)
        post.save()
        
        
    return render(request, 'pages/write_success.html', {'name': name})
    
    
def write_comment(request):
    if request.method == "POST":
        writer = request.POST.get('writer')
        message = request.POST.get('message')
        post_id = request.POST.get('post')
        post = Post.objects.get(pk=post_id)
        comment = Comment(writer=writer, message=message, post=post)
        comment.save()
        
        request.session['name'] = writer

        return redirect('list')
    

def edit(request, id):
    post = get_object_or_404(Post, pk=id)
            
    return render(request, 'pages/edit.html', {'post': post})


def update(request):
    id = request.POST.get('pk')
    post = get_object_or_404(Post, pk=id)
    
    content = request.POST.get('content')
    
    if request.FILES.get('file'):
        image = request.FILES['file']
        post.img = image
    
    if request.POST.get('checkbox'):
        post.img = None
    
    post.content = content
    
    if post.is_dirty():
        post.is_edited = True
    
    # pdb.set_trace()
    
    post.save()
    
    return redirect('update_success')


def update_success(request):
    
    return render(request, 'pages/update_success.html')
    
    
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    
    return redirect('delete_success')


def delete_success(request):
    
    return render(request, 'pages/delete_success.html')
    

def verification(request):

    return render(request, 'pages/verification.html')


def check_pwd(request):
    id = request.POST.get('id')
    post = get_object_or_404(Post, pk=id)
    
    pwd = request.POST.get('password')
    
    if pwd == post.password:
        if request.POST.get('action') == "edit":
            return redirect('edit', id)
        
        else:
            return redirect('delete', id)
            
    else:
        return redirect('fail')
        

def fail(request):
    
    return render(request, 'pages/fail.html')