
import setuptools


setup_params = dict(
    author='Alex Malykh',
    author_email='a2m.dev@yandex.ru',
    name='cmsplugin-css-background',
    use_scm_version=dict(root='.', relative_to=__file__),
    description='A django CMS plugin for managing CSS background styles',
    license='MIT License',
    url='https://github.com/alexmalykh/cmsplugin-css-background',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['django-cms>=3.3,<4.0', 'six'],
    setup_requires=['setuptools_scm'],
    zip_safe=False
)


if __name__ == '__main__':
    setuptools.setup(**setup_params)
