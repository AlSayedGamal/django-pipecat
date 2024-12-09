=====
Usage
=====

To use django-pipecat in a project, add it to your `INSTALLED_APPS`:

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
