=============================
django-pipecat
=============================

.. image:: https://badge.fury.io/py/django-pipecat.svg
    :target: https://badge.fury.io/py/django-pipecat

.. image:: https://travis-ci.org/alsayedgamal/django-pipecat.svg?branch=master
    :target: https://travis-ci.org/alsayedgamal/django-pipecat

.. image:: https://codecov.io/gh/alsayedgamal/django-pipecat/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/alsayedgamal/django-pipecat

pipecat's pipeline wrapper for django

Documentation
-------------

The full documentation is at https://django-pipecat.readthedocs.io.

Quickstart
----------

Install django-pipecat::

    pip install django-pipecat

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_pipecat.apps.DjangoPipecatConfig',
        ...
    )

Add django-pipecat's URL patterns:

.. code-block:: python

    from django_pipecat import urls as django_pipecat_urls


    urlpatterns = [
        ...
        url(r'^', include(django_pipecat_urls)),
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


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
