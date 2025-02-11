from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from app_teaching.models import *
import random

# Create your views here.
def index_view(request):
    Posts = Post.objects.filter(published__lte = timezone.now())
    for item in Posts:
        item.views += 1
        item.save()
    context={'posts': Posts}
    return render(request, 'index.html', context)