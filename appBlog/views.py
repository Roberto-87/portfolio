# from http.client import HTTPResponse
# from django.shortcuts import render,get_object_or_404
# from .models import Post


# def home_blog (request):
#     post= Post.objects.all()
#     return render(request, 'home_blog.html',{
#         'posts': post
#     })

# def post_detail(request,post_id):
#     post= get_object_or_404(Post, pk=post_id)
#     return render (request, 'post_detail.html', {'post':post})