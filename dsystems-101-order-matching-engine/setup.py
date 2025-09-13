from setuptools import setup, find_packages

setup(
    name="DSystems 101: Build a Distributed Order Matching Engine",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Distributed pub-sub system for trading and notifications",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dsystems-101-order-matching-engine",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "kafka-python",
        "redis",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)