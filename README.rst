cmsplugin-css-background
========================
.. _django CMS: https://django-cms.org
.. _django-sekizai: http://django-sekizai.readthedocs.io
.. _cmsplugin-filer: https://github.com/divio/cmsplugin-filer

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

1. Define a placeholder in your template like this:

   .. code:: django

    {% with css_selector='#some-element' %}
        {% placeholder 'Placeholder Name' %}
    {% endwith %}

   The placeholder can be anywhere but it is recommended to keep it near the
   element specified by the CSS selector. Note that the selector can be any
   valid CSS selector, not just an id.

2. Add an instance of ``CSS Background`` from the ``Generic`` plugin group to the
   created placeholder on your page in the CMS admin.

   .. note::
      This package is aware of `cmsplugin-filer`_. If it is
      installed and enabled, then you also get extra ``CSS Background`` plugin
      available in the ``Filer`` plugins group. This allows you to use images
      managed by Filer.

3. Configure the required background CSS styling that will be applied to the
   element. All fields may be left blank if not required, but at least
   color or image must be provided. Omitted properties cascade down
   to corresponding lower-priority styling.

The CSS style definition is added to the sekizai ``css`` block in the ``<head/>``
element, in compliance with W3 specs:

.. code:: html

    <style type="text/css">
    #some-element {
        /* here 'background-' CSS rules go */
        ...
    }
    </style>

The template used is `cmsplugin_css_background/css-background.html
<cmsplugin_css_background/templates/cmsplugin_css_background/css-background.html>`_.

By default, background properties are rendered as a list of separate rules
(which are omitted if not specified), but there is a shorthand option too.
To use it just override ``cmsplugin_css_background/css-background.html`` template
somewhere in your project tree and replace

.. code:: django

    {{ instance.as_separate_rules }}

with

.. code:: django

    {{ instance.as_single_rule }}

.. note::
   Using the shorthand property is not recommended because empty properties will
   fall back to default values defined in W3 specs, thus preventing cascading
   down to lower-priority rules (it they are defined). This is normal for CSS,
   but in some cases it might be not what you're expecting.

.. Translations
.. ~~~~~~~~~~~~
.. you can help to translate this plugin at Transifex
