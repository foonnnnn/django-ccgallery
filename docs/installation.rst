Installation
=====================================

Install via pip:

.. code-block:: bash

   pip install django-ccgallery


Next add ``ccgallery`` to your settings.INSTALLED_APPS::

    INSTALLED_APPS = (
        #...
        'ccgallery',
        #...
    )

If ``ccthumbs`` isn't listed in your settings.INSTALLED_APPS then you will
also have to add ``ccthumbs``:: 

    INSTALLED_APPS = (
        #...
        'ccthumbs',
        #...
    )

.. note:: ``ccthumbs`` needs only be listed **once** so there is no need to add it if it is already present.
 
Now do a ``syncdb``:

.. code-block:: bash

    python manage.py syncdb

Now do a ``collectstatic``:

.. code-block:: bash

    python manage.py  collectstatic

You're all done.
