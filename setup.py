import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '0.1.3.dev0'

install_requires = [
    'Kotti>=0.10b1',
]


setup(
    name='kotti_bootswatch',
    version=version,
    description="Kotti bootswatch theme / theme generator",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='mete0r',
    author_email='kotti@googlegroups.com',
    url='https://github.com/mete0r/kotti_bootswatch',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
        'fanstatic.libraries': [
            'kotti_bootswatch = kotti_bootswatch.fanstatic:library',
        ],
        'pyramid.scaffold': [
            'kotti_bootswatch = kotti_bootswatch.scaffolds:ThemeTemplate',
        ],
    },
    extras_require={},
)
