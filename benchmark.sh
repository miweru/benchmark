#!/usr/bin/env bash
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
/usr/bin/env python3 -m venv $tmp_dir
source $tmp_dir/bin/activate
pip install -U setuptools wheel git+https://github.com/miweru/benchmark
