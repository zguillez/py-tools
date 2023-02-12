import pathlib
from setuptools import setup, find_packages


setup(
        name='py-tools',
        version='0.1.0',
        author='Guillermo de la Iglesia',
        author_email='mail@zguillez.io',
        description='Pyton helpers',
        long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
        long_description_content_type='text/x-rst',
        url='https://github.com/zguillez/py-tools',
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            'numpy',
            'pandas',
        ],
)
