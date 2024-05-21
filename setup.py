from setuptools import setup, find_packages

setup(
    name="fastapi_project",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "pytest",
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'start-fastapi=app.main:main',  # This creates a command line entry point to start the app
        ],
    },
    package_data={
        '': ['*.md', '*.txt', '*.log'],
    },
    author="Dinesh Panajkar",
    author_email="dpanajkar1@gmail.com",
    description="A FastAPI project for addition of integers in lists",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
