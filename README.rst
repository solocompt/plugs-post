=============================
Plugs Post
=============================

.. image:: https://badge.fury.io/py/plugs-post.png
    :target: https://badge.fury.io/py/plugs-post

.. image:: https://travis-ci.org/yo-solo/plugs-post.png?branch=master
    :target: https://travis-ci.org/yo-solo/plugs-post

Quick start
-----------

1. Install using Pip

   .. code-block:: bash

                   $ pip install plugs_post

2. Add it to INSTALLED_APPS

   .. code-block:: python

                   INSTALLED_APPS = (
                   # other apps
                   'plugs_post'
                   )

3. Run migrate

   .. code-block:: bash

                   $ python manage.py migrate plugs_post

4. Register the Viewsets

   .. code-block:: python

                   from plugs_post.views import PostViewSet, PostSectionViewSet

                   ROUTER = routers.DefaultRouter()

                   ROUTER.register(r'posts', PostViewSet)
                   ROUTER.register(r'post_sections', PostSectionViewSet)

                   urlpatterns = [
                   url(r'^', include(ROUTER.urls))
                   ]
