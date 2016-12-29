=====
Usage
=====

To use Plugs Posts in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_post.apps.PlugsPostConfig',
        ...
    )

Add Plugs Posts's URL patterns:

.. code-block:: python

    from plugs_post import urls as plugs_post_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_post_urls)),
        ...
    ]
