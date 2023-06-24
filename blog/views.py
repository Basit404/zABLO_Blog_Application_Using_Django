from django.shortcuts import render, HttpResponse
from blog.models import Blog, Feedback
import math
# Create your views here.

# function for homepage
def home(request):
    return render(request, "home.html")

# function for blog page
def blog(request):
    # logic for pagination
    no_of_posts = 4
    page = request.GET.get("page")
    if page is None:
        page = 1
    else:
        page = int(page)

    '''
    1: 0 - 3
    2: 3 - 6
    3: 6 - 9

    1: 0 - 0 + no_of_posts
    2: no_of_posts to no_of_posts + no_of_posts
    3: no_of_posts + no_of_posts to no_of_posts + no_of_posts + no_of_posts

    (page_no -1) * no_of_posts to page_no * no_of_posts
    '''

    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = Blog.objects.all()[(page-1) * no_of_posts: page * no_of_posts]
    if page > 1:
        prev = page - 1
    else:
        prev = None

    if page < math.ceil((length / no_of_posts)):
        nxt = page + 1
    else:
        nxt = None

    context = {
        'blogs': blogs,
        'prev': prev,
        'nxt': nxt
    }
    return render(request, "blog.html", context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, "blogpost.html", context)

# function for feedback section
def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Feedback(name=name, email=email, phone=phone, desc=desc)
        instance.save()
    return render(request, "feedback.html")

# function for about page
def about(request):
    return render(request, "about.html")
