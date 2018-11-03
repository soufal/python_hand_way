try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project',
    'author': 'Soufal',
    'url': 'github/soufal.com',
    'download_url': '',
    'author_email': 'wyf3510@126.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'test'
}

setup(**config)
