from setuptools import setup, find_packages

setup(
    name = 'compropago-python',
    description = 'Python library for ComproPago',
    version = '0.1',
    packages = find_packages(),
    author = 'Noe Nieto',
    author_email = 'nnieto@noenieto.com',
    license = 'MIT',
    url = 'http://github.io/tzicatl/compropago-python',
    install_requires = ['requests',],
    tests_require = ['nose>=1.0', 'responses'],
)
