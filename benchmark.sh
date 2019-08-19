#!/usr/bin/env bash
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
/usr/bin/env python3 -m venv $tmp_dir
source $tmp_dir/bin/activate
pip install -U setuptools wheel
pip install somajo==1.10.5 scikit-learn==0.21.3 scipy==1.3.1
pip install git+https://github.com/miweru/benchmark
