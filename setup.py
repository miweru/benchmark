#!/usr/bin/env python3
import os, sys
from setuptools import setup

setup(
    name="mipythonbenchmark",
    version="0.0.1",
    scripts="pybenchmark",
    install_requires=[
    "somajo==1.10.5",
    "scikit-learn==0.21.3",
    "scipy==1.3.1"],
)
