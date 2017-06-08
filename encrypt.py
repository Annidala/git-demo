#!/usr/bin/python3
from __future__ import print_function

import sys

if sys.version_info.major < 3:
  input = raw_input

def encrypt(in_file,out_file):
  with open(in_file,"rb") as f:
    content = bytearray(f.read())
  for i,b in enumerate(content):
    content[i] = 255 ^ b
  with open(out_file,"wb") as f:
    f.write(content)

if __name__ == "__main__":
  f_in = input("File to encrypt?> ")
  f_out = input("File to write (will be overwritten!)> ")
  encrypt(f_in,f_out)
