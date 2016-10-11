cmsplugin-css-background
========================
.. _django CMS: https://django-cms.org
.. _django-sekizai: http://django-sekizai.readthedocs.io

`django CMS`_ plugin for configuring background images in edit mode via CSS
rules.


Requirements
------------

    * Django 1.8+
    * django CMS 3.3+

Installation
------------

In your Python environment run

.. code:: shell

    $ pip install cmsplugin-css-background

This will install the latest stable version of the plugin package.
To install the package's latest repository snapshot run

.. code:: shell

    $ pip install -e git+https://github.com/alexmalykh/cmsplugin-css-background.git@master#egg=cmsplugin-css-background

Then add the plugin to ``INSTALLED_APPS`` list:

.. code:: python

    INSTALLED_APPS = [
        ...,
        'cmsplugin_css_background',
    ]

and finally, roll database migrations:

.. code:: shell

    $ python manage.py migrate cmsplugin_css_background


Usage
-----

1. Define a placeholder in your template this way:

   .. code:: django

    {% with css_selector = '#some-element' %}
        {% placeholder 'some_element_background' %}
    {% endwith %}


   The placeholder might be located almost anywhere, not necessarily
   within/beside the element you want to change background. But it is
   recommended to keep both together for convenience.

   Optionally, you might add an entry for your placeholder
   to ``PLACEHOLDER_CONF`` settings dictionary to restrict allowed plugin types
   to ``CSS Background`` and assign a readable title to the placeholder's
   dragbar instead of generated **Some_Element_Background**.

2. Add an instance of ``CSS Background`` from the ``Generic`` plugin group to the
   placeholder in CMS admin.

   .. note::
      This package is aware of ``cmsplugin-filer``. If the latter is
      installed and enabled, then you also get extra ``CSS Background`` plugin
      available in ``Filer`` plugins group. This option allows you to use images
      managed by Filer.

The plugin is rendered as ``<style />`` HTML element in-place, like this:

.. code:: html

    <style type="text/css">
    #some-element {
        /* here 'background-' CSS rules go */
        ...
    }
    </style>

but it is possible to make the plugin render in HTML ``<HEAD/>`` section
to keep compliance with W3 standards: just wrap the containing placeholder
in django-sekizai_'s ``addtoblock`` tag and then render corresponding
block with ``render_block``:

.. code:: Django

    {% addtoblock 'css' %}
    {% with css_selector = '#some-element' %}
        {% placeholder 'some_element_background' %}
    {% endwith %}
    {% endaddtoblock }

There is a single template, located at
``cmsplugin_css_background/css-background.html`` and it takes a single extra
context variable ``css_selector`` which defines the element(s) to assign
background settings.

By default, background properties are rendered as a list of separate rules,
but there is one-liner option too. To change the way plugin rendered
override the plugin template and replace

.. code:: django

    {{ instance.as_separate_rules }}

with

.. code:: django

    {{ instance.as_single_rule }}


.. Translations
.. ~~~~~~~~~~~~
.. you can help to translate this plugin at Transifex
