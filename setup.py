from setuptools import setup, find_packages

setup(
    name="job-extractor",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "playwright==1.44.0",
        "pydantic==2.7.4",
    ],
    extras_require={
        "dev": [
            "pytest==8.2.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "job-extractor=job_extractor.main:main",
        ],
    },
)
