#!/usr/bin/python3
from __future__ import print_function

def encrypt(in_file,out_file,key=[255]):
  """
  This function takes a file a xor each byte with 255
  It will then write this "anti-file" to the disk
  NOTE: the file is loaded and written in one pass, so its size should not
  exceed the available memory!
  args:
    in_file (str): Name of the input file
    out_file (str): Name of the output file
  """
  with open(in_file,"rb") as f:
    content = bytearray(f.read()) # bytearrays are mutable unlike bytes
  for i,b in enumerate(content):
    content[i] = b ^ key[i%len(key)] # ^ means bitwise XOR
  with open(out_file,"wb") as f:
    f.write(content)

if __name__ == "__main__":
  import sys
  if sys.version_info.major < 3:
    # For input to return a string and not execute the input in Python 2
    input = raw_input
  # If calling the file directly: prompt the files and run it once
  f_in = input("File to encrypt?> ")
  f_out = input("File to write (will be overwritten!)> ")
  key = input("Key? (leave empty for 255)> ").encode("utf-8") or [255]
  encrypt(f_in,f_out,key)
