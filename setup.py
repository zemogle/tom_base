from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tomtoolkit',
    version='1.2.4',
    description='The TOM Toolkit and base modules',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://tomtoolkit.github.io',
    author='TOM Toolkit Project',
    author_email='ariba@lco.global',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords=['tomtoolkit', 'astronomy', 'astrophysics', 'cosmology', 'science', 'fits', 'observatory'],
    packages=find_packages(),
    install_requires=[
        'django<3.0',
        'django-bootstrap4',
        'django-extensions',
        'django-filter',
        'django-contrib-comments',
        'django-gravatar2',
        'django-crispy-forms',
        'django-guardian',
        'numpy',
        'python-dateutil',
        'requests',
        'astroquery',
        'numpy==1.7.4',
        'astropy==3.2.1',
        'astroplan',
        'plotly',
        'matplotlib',
        'pillow',
        'fits2image',
        'specutils',
        'dataclasses; python_version < "3.7"',
    ],
    extras_require={
        'test': ['factory_boy']
    },
    include_package_data=True,
)
