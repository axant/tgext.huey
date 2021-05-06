from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

version = "0.0.1"

setup(
    name='tgext.huey',
    version=version,
    description="",
    long_description=README,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='turbogears2.extension',
    author='Francesco Vallone',
    author_email='francesco.vallone@axant.it',
    url='https://github.com/axant/tgext.huey.git',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages = ['tgext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "TurboGears2 >= 2.4.3",
        "gearbox",
        "PasteDeploy",
        "huey == 2.3.2",
    ],
    extras_require={
        "redis": [
            "redis == 3.5.3"
        ]
    },
    entry_points={
    }
)
