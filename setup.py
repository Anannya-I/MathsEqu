from setuptools import setup, find_packages

setup(
    name='mathsequals',  # Change this to your desired package name
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    author='Your Name',
    author_email='you@example.com',
    description='A short description of the package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',  # Update this
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
