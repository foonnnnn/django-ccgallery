Configuration
============================

Here are the available configuration options available to customise ccgallery.

Settings
-----------------

CCGALLERY_ITEM_DEFAULT_STATUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An ``integer`` that dictates whether or not newly created gallery items are visible or hidden. The default is ``1`` which is visible. Change this to ``0`` to dicate hidden.

CCGALLERY_CATEGORY_DEFAULT_STATUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An ``integer`` that dictates whether or not newly created gallery category are visible or hidden. The default is ``1`` which is visible. Change this to ``0`` to dicate hidden.

CCGALLERY_MODEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A ``django.db.models.Model`` that you want to use instead of the default ``cccgallery.models.Item`` model. Your model must implement a custom manager that defines methods for ``visible()`` and ``hidden()``.

The default is::

    ccgallery.models.Item

CCGALLERY_IMAGE_SIZES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``tuple`` of ``tuples``, each of which contains a width and a height.

The default is::

        ((200,200),
        (640, 480),
        (1200, 960))
