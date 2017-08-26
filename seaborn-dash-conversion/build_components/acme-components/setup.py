from setuptools import setup

exec (open('acme_components/version.py').read())

setup(
    name='acme_components',
    version=__version__,
    author='usyyy',
    packages=['acme_components'],
    include_package_data=True,
    license='MIT',
    description='Components used by the Acme Corp',
    install_requires=[]
)
