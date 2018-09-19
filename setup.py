# Created by Les1ie on 2018/9/19.
# Email: me@les1ie.com

import setuptools
import platform

os = platform.platform()
def set_scripts():
    os = platform.system()
    if os=='Windows':
        return ['scunet.bat']
    else:
        return ['SCUNET/SCUNET.py']

with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setuptools.setup(
    name="pyscunet",
    version="0.0.1",
    author="Les1ie",
    author_email="me@les1ie.com",
    description="login scunet in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/iansmith123/SCUNET',
    packages=setuptools.find_packages(),
    license="GPL v3",
    install_requires=[
        'requests',
        'nobug'
    ],
    scripts=set_scripts(),
    classifier=[
        "Programming Language :: Python :: 3",
        "Topic :: Utilities"
    ]
)
