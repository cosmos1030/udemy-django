from django.shortcuts import render

mydic = {1: 'first post', 2: 'second post', 3: 'third post'}

# Create your views here.
def index(request):
    return render(request, 'blog/index.html',
    {'mydic': mydic})