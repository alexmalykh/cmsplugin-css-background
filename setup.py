
import io
import setuptools


with io.open('README.rst', 'r') as readme:
    try:
        long_description = readme.read()
    except IOError:
        long_description = ''


setup_params = dict(
    author='Alex Malykh',
    author_email='a2m.dev@yandex.ru',
    name='cmsplugin-css-background',
    use_scm_version=dict(root='.', relative_to=__file__),
    description='A django CMS plugin for managing CSS background styles',
    long_description=long_description,
    license='MIT License',
    url='https://github.com/alexmalykh/cmsplugin-css-background',
    packages=setuptools.find_packages(),
    install_requires=['django-cms>=3.3,<4.0', 'six'],
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)


if __name__ == '__main__':
    setuptools.setup(**setup_params)
