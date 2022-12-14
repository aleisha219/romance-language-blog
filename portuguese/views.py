from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'portuguese/post_list.html', {'posts':posts})