=============================
Plugs Post
=============================

.. image:: https://badge.fury.io/py/plugs-post.png
    :target: https://badge.fury.io/py/plugs-post

.. image:: https://travis-ci.org/ricardolobo/plugs-post.png?branch=master
    :target: https://travis-ci.org/ricardolobo/plugs-post

Quick start
-----------

Soon...

...

from plugs_post.views import PostViewSet, PostSectionViewSet

ROUTER = routers.DefaultRouter()

...

ROUTER.register(r'posts', PostViewSet)
ROUTER.register(r'post_sections', PostSectionViewSet)

...

urlpatterns = [
    url(r'^', include(ROUTER.urls))
]
