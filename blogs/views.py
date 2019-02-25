from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
import blogs.blogservice as blogservice
from blogs.models import Post

from blogs.serializers import UserSerializer, GroupSerializer, PostSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the blogs index.")


def hello(request):
    name = request.GET.get("name")
    return HttpResponse("Hello," + name + "! Nice to meet you.")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint to post a new blog value given some text
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, url_path="postblog",methods=['post', 'put'])
    def add_blog(self, request, pk=None):
        blogservice.add_blog(request.data['blogtext'])
        return HttpResponse({"created": True})
