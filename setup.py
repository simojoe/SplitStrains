from setuptools import setup

from SplitStrains import __version__, _program

setup(
    name=_program,
    version=__version__,
    author="Einar Gabbasov",
    author_email="",
    description="SplitStrains detects and separates mixed strains of Mycobacterium tuberculosis.",
    url="https://github.com/WGS-TB/SplitStrains",
    license="",
    packages=["SplitStrains"],
    entry_points="""
    [console_scripts]
    {program} = SplitStrains.splitStrains:main
    """.format(program=_program),
    include_package_data=True,
    install_requires=[
        "matplotlib>=3.3",
        "mixem",
        "numpy",
        "pysam",
        "scikit-learn",
        "scipy",
        "sns",
    ],
)
