import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml_colon",
    version="1.0",
    author="somebody",
    author_email="me@idontcare.com",  # TODO
    description="A ml pipeline for colon image data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agemcipe/data_processes_mlcolonoscopy",
    setup_requires=["setuptools_scm"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
