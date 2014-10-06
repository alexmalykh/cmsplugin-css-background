
from setuptools import find_packages, setup
import cmsplugin_css_background

setup(
    author='Alex Malykh',
    author_email='a2m.dev@yandex.ru',
    name='cmsplugin-css-background',
    version=cmsplugin_css_background.__version__,
    description='A Django CMS plugin for managing CSS background styles',
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django-cms >= 3.0'],
    zip_safe=False
)
