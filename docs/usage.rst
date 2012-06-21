Usage
================================

.. note:: These instructions assume that you're using the bundled ``Item`` model, the bundled lightbox plugin (FancyBox_) and are using the supplied templates or your own versions that are "close enough" to the originals.


Gallery Items
-----------------------

Gallery items are created and edited via the django admin panel.

A gallery item can have the following properties

* **Name** –  a ``string`` accessible via ``item.name``
* **Slug** –  a ``SlugField`` accessible via ``item.slug``
* **description** –  a ``TextField`` accessible via ``item.description``
* **order** –  a ``DecimalField`` accessible via ``item.order``
* **created** –  a ``DateTimeField`` accessible via ``item.created``
* **status** –  a ``PositiveSmallIntegerField`` accessible via ``item.status``


A gallery item has the following relationships

* **Categories** –  a ``ManyToMany`` relationship accessibled via ``item.categories``


Gallery Categories
-----------------------

Gallery categories are created and edited via the django admin panel.


.. _`FancyBox`: http://fancybox.net/

