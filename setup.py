from setuptools import find_packages, setup

setup(
    name='denoising',
    packages=find_packages(),
    version='0.1.0',
    description='denoising library that i\'ve worked on in my summer internship',
    author='Meryem Mine Gündoğan',
    install_requires=[
        'numpy',
        'scikit-image',
        'opencv-python',
        'matplotlib'
    ]
)