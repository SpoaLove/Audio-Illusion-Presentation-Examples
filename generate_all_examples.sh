#!/bin/bash

set -x  # Enable execution trace

experiments=("deutsch_1975_1a" "deutsch_1975_1b" "deutsch_1975_1c" "deutsch_1975_discussion" "deutsch_1974")

for experiment in "${experiments[@]}"; do
    python generate_wav.py save "$experiment"
    python generate_wav.py save "$experiment" -r
done