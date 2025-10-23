#!/usr/bin/env python3

import sys
from lib_csv import encode_file
from lib_csv import restore_file

if len(sys.argv) < 2:
    print("Usage: python encoder_csv.py <input_file>")
    sys.exit(1)

encode_file(sys.argv[1])
