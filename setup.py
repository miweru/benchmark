#!/usr/bin/env python3
import os, sys
from distutils.core import setup
from distutils.command.install import install as _install


def _post_install(dir):
    #os.system("pybenchmark")
    print("NOTHING")

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")


setup(
    name="mipythonbenchmark",
    version="0.0.1",
    scripts="pybenchmark",
    install_requires=[
    "somajo==1.10.5",
    "scikit-learn==0.21.3",
    "scipy==1.3.1"],
    cmdclass={'install': install},
)
