cmsplugin-css-background
========================
.. _django CMS: https://django-cms.org

`django CMS`_ plugin for configuring background images in edit mode via CSS
rules.


Requirements
------------

Have a look in `requirements.txt <requirements.txt>`_

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

Ensure ``CMS_PLACEHOLDER_CONF`` is configured to allow one or both of: 
``CssBackgroundPlugin``, ``FilerCssBackgroundPlugin``

and finally, roll database migrations:

.. code:: shell

    $ python manage.py migrate cmsplugin_css_background


Usage
-----

1. Add an instance of ``CSS Background`` from the ``Generic`` plugin group to a
   placeholder on your page in the CMS admin.
   
   .. Note::
      This package is aware of ``cmsplugin-filer``. If the latter is
      installed and enabled, then you also get extra ``CSS Background`` plugin
      available in ``Filer`` plugins group. This option allows you to use images
      managed by Filer.

2. Configure the background, id and class CSS styling that will be applied to the
   div element wrapper added by the plugin. All fields may be left blank if not
   required except there must be either a color or image specified (otherwise there
   seems little point adding this plugin!).

3. Add or rearrange existing CMS plugins as children to the background plugin.

The plugin is rendered as an inline ``<div>`` HTML element like this:

.. code:: html

    <div id="one" class="bg" style="background-image: url(bg12.jpg);">
        <!-- Child plugins here -->
        <div class="container">
            <div class="row">
                ...
            </div>
        </div>
    </div>

The template used is ``cms/plugins/css-bgwrapper.html``.

By default, background properties are rendered as a list of separate rules,
but there is shorthand option too. To use this create your own plugin that inherits
from ours and override the template with your own replacing

.. code:: django

    {{ instance.as_separate_rules|safe }}

with

.. code:: django

    {{ instance.as_single_rule|safe }}

.. Note::
  Using the shorthand property is not recommended because empty properties will
  inherit their default values and override less specific CSS properties, as normal
  for CSS.

.. Translations
.. ~~~~~~~~~~~~
.. you can help to translate this plugin at Transifex

