import view as view
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Post, Like


def home(request):
    post=Post.objects.all()
    context={
        'post':post
    }
    return render(request,"home.html",context)

class PostViewset(viewsets.ModelViewSet):

    queryset=Post.objects.all()

def like(request):
	post_id = request.GET.get("likeId", "")
	user = request.user
	post = Post.objects.get(pk=post_id)
	liked= False
	like = Like.objects.filter(user=user, post=post)
	if like:
		like.delete()
	else:
		liked = True
		Like.objects.create(user=user, post=post)
	resp = {
        'liked':liked
    }
	response = json.dumps(resp)
	return HttpResponse(response, content_type = "application/json")



