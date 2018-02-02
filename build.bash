#!/bin/bash
outfile=${1:-creatures.md}
python report.py > "$outfile"
