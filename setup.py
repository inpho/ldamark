from setuptools import setup, Extension, Command, find_packages
import platform
import wget
import tarfile

# find packages in vsm subdirectory
# this will skip the unittests, etc.
packages = ['ldamark.'+pkg for pkg in find_packages('ldamark')]
packages.append('ldamark')

# TODO need to add mallet download
mallet_zip = wget.download('http://mallet.cs.umass.edu/dist/mallet-2.0.8RC3.tar.gz')
mallet_dir = tarfile.open(mallet_zip, "r:gz")
mallet_dir.extractall()
mallet_dir.close()

install_requires=[
    "numpy>=1.6.1",
    "scipy>=0.13.0",
    "topicexplorer",
    ]

setup(
    name = "ldamark",
    version = "0.1",
    description = ('LDA Benchmarking Project'),
    author = "InPhO",
    author_email = "inpho@indiana.edu",
    url = "http://inphodata.cogs.indiana.edu",
    download_url = "https://github.com/inpho/ldamark",
    keywords = [],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        ],
    install_requires=install_requires,
    packages=packages,
    entry_points={
        'console_scripts' : ['ldamark = ldamark.benchmark:main']
    }
)
