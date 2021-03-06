
from setupbase import create_cmdclass, __version__
from setuptools import find_packages, setup
import sys


setup_args = dict(
    name='newlab',
    version=__version__,
    packages=find_packages('.'),
    description='JupyterLab Server',
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    author='LATEEFROCKZ',
    author_email='2012lateef@gmail.com',
    url='https://jupyter.org',
    platforms='Linux, Mac OS X, Windows',
    keywords=['Jupyter', 'JupyterLab'],
    cmdclass=create_cmdclass(),
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True
)

if 'setuptools' in sys.modules:
    setup_args['python_requires'] = '>=3.5'
    setup_args['extras_require'] = {'test': ['pytest', 'requests']}
    setup_args['install_requires'] = [
        'json5',
        'jsonschema>=3.0.1',
        'notebook>=4.2.0',
        'jinja2>=2.10'
    ]

if __name__ == '__main__':
    setup(**setup_args)
