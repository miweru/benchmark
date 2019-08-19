#!/usr/sys/env bash
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
/usr/sys/env python3 -m venv $tmp_dir
source $tmp_dir/bin/activate
pip install git+https://github.com/miweru/benchmark
