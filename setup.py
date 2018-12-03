# Created by Les1ie on 2018/9/19.
# Email: me@les1ie.com

import setuptools
import platform
import os

system = platform.system()

# 影响打包的复制，暂时注释
"""
def set_scripts():
    if system == 'Windows':
        return [os.path.join("script", 'scunet.bat'), os.path.join("script", "scunet.py")]
    else:
        return ['scunet', os.path.join("script", "scunet.py")]
        # return [os.path.join('script', 'scunet'), os.path.join("script", "scunet.py")]

"""


def set_scripts():
    return [
        os.path.join("script", "scunet"),
        os.path.join("script", "scunet.bat"),
        os.path.join("script", "scunet.py"),
    ]


def set_require():
    if system == "Windows" and platform.release() == 10:
        return ['win10toast', 'requests']
    else:
        return ['requests']


with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setuptools.setup(
    name="scunet",
    version="1.1.0",
    author="Les1ie",
    author_email="me@les1ie.com",
    description="login scunet in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/iansmith123/SCUNET',
    packages=setuptools.find_packages(),
    license="GPL v3",
    install_requires=set_require(),
    scripts=set_scripts(),
)
