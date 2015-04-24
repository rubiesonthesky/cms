from blog.api import BlogViewSet, PostViewSet
from blog.views import BlogListView, BlogDetailView, PostListView, PostDetailView
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='blog-list'),
    url(r'^(?P<pk>[0-9]+)/$', BlogDetailView.as_view(), name='blog-detail'),
    url(r'^(?P<blog_id>[0-9]+)/posts/$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<blog_id>[0-9]+)/posts/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^api/', include(router.urls))
]