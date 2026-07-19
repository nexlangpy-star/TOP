from setuptools import setup, find_packages
import os

setup(
    name="TOP",
    version="1.3.2",
    packages=find_packages(),
    install_requires=[],
    author="devil",
    description="BETA 1.2",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_data={
        'TOP': ['*.so'],
    },
    include_package_data=True,
    data_files=[
        ('lib', ["TOP/TOP.cpython-313.so"]),
    ],
    zip_safe=False,
)