import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openssltool",
    version="0.0.1",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="run openssl via python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/openssltool",
    project_urls={
        "Bug Tracker": "https://github.com/Madhava-mng/openssltool",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

