import setuptools

setuptools.setup(
    name="ClusterBoss", 
    version="0.1",
    author="Katharine Long",
    author_email="katharine.long@ttu.edu",
    description="Distributed job execution",
    long_description="Distributed execution of a set of function evaluations",
    long_description_content_type="text/markdown",
    url="https://github.com/krlong014/CllusterBoss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: LGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
