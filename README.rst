=============================
Plugs Posts
=============================

.. image:: https://badge.fury.io/py/plugs-post.png
    :target: https://badge.fury.io/py/plugs-post

.. image:: https://travis-ci.org/ricardolobo/plugs-post.png?branch=master
    :target: https://travis-ci.org/ricardolobo/plugs-post

Your project description goes here

Documentation
-------------

The full documentation is at https://plugs-post.readthedocs.io.

Quickstart
----------

Install Plugs Posts::

    pip install plugs-post

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
