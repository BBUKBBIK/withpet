from .models import Blog, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .form import Postform
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def comment_write(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Blog, pk=post_pk)
        content = request.POST.get('content')
        if not content:
            messages.info(request, "You dont write anything...")
            return redirect('/post/' + str(post_pk))

        Comment.objects.create(post_key = post, comment_contents=content)
        return redirect('/post/'+str(post_pk))

def delete1(request, comment_id, post_id):
    comment = get_object_or_404(Comment , pk = comment_id )
    comment.delete()
    return redirect('/post/'+str(post_id))


def delete(request, post_id):
    post = get_object_or_404(Blog, pk = post_id)
    post.delete()
    return redirect('home')

def post(request, post_id):
    post_detail = get_object_or_404(Blog, pk=post_id)
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user.get_username())
        return render(request, 'post.html', {'post':post_detail, 'user':user})
    else:
        return render(request, 'post.html', {'post':post_detail})

def home(request):
    posts = Blog.objects.all().order_by('-id')

    return render(request, 'home.html', {'posts_show':posts})

def modify(request, post_id):
    post = Blog.objects.get(id=post_id)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post.title = form.cleaned_data['title']   
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('/post/' +str(post_id))
    else:
        form= Postform(instance=post)
        return render(request,'modify.html',{'form':form})