#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

extras_require = {
    'eth-signer':[
        "eth_account>=0.9.0",
        "pycryptodome>=3.19.1",
        "boto3>=1.34.69",
    ],
    'test': [
        "pytest>=8.1.1",
    ],
    'lint': [
        "flake8>=7.0.0",
        "isort>=5.13.2",
        "mypy>=1.9.0",
    ],
    'docs': [
        "Sphinx>=7.2.6",
        "sphinx_rtd_theme>=2.0.0",
        "towncrier>=23.11.0",
    ],
    'dev': [
        "bumpversion>=0.6.0",
        "setuptools>=69.2.0",
        "tox>=4.14.1",
        "twine>=5.0.0",
    ]
}

extras_require['dev'] = (
    extras_require['test']
    + extras_require['lint']
    + extras_require['docs']
    + extras_require['dev']
)

with open('./README.md') as readme:
    long_description = readme.read()

setup(
    name='eth-signer',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.1.10',
    description="""A Python library for transection signing using AWS Key Management Service.""",
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Kalpesh Sejpal',
    author_email='sejpalkalpesh@gmail.com',
    url='https://github.com/sejpalkalpesh/eth-signer',
    include_package_data=True,
    install_requires=extras_require['eth-signer'],
    python_requires='>=3.6,<4',
    extras_require=extras_require,
    py_modules=['eth_signer'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum AWS KMS,',
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"eth_signer": ["py.typed"]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
