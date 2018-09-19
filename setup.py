# Created by Les1ie on 2018/9/19.
# Email: me@les1ie.com

import setuptools
import platform



def set_scripts():
    if platform.system() == 'Windows':
        return ['scunet.bat', "SCUNET/SCUNET.py"]
    else:
        return ['SCUNET/SCUNET.py']


with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setuptools.setup(
    name="scunet",
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
        # 'requests',
        # 'nobug'
    ],
    scripts=set_scripts(),
    classifier=[
        "Programming Language :: Python :: 3",
        "Topic :: Utilities"
    ]
)
