try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Test Project',
    'author': 'Murugesan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose', 'numpy'],
    'packages': ['hr_python.easy'],
    'scripts': [],
    'name': 'hr_python'
}

setup(**config, install_requires=['numpy'])
