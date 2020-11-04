#!/usr/bin/env python
import argparse, sys, io, re

PYTEX_PATTERN = r'(?s)🐍(.*?)🐍'

def collect_stdout_from_executable(exec_string, local_scope={}, global_scope={}):
  old_stdout = sys.stdout
  redirected_output = sys.stdout = io.StringIO()
  try:
    exec(exec_string, global_scope, local_scope)
  except: raise 
  finally:
    sys.stdout = old_stdout
  return redirected_output.getvalue()

def pytex_to_tex(pytex):
  local_scope, global_scope = {}, {}
  tex = re.sub(PYTEX_PATTERN,
               lambda match: collect_stdout_from_executable(match.group(1),
                                                            local_scope,
                                                            global_scope),
               pytex)
  return tex

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Converts .pytex files into .tex files..')
  parser.add_argument('infile', help="The source pytex file.")
  parser.add_argument('outfile', help="The destination tex file.")

  infile = parser.parse_args().infile
  outfile = parser.parse_args().outfile

  # Read the infile
  with open(infile, 'r') as in_f:
    # Write to the outfile    
    with open(outfile, 'w') as out_f:
      out_f.write(pytex_to_tex(in_f.read()))

"""
Highlight with the following .sublime-syntax file:

%YAML 1.2
---
file_extensions: [pytex]
scope: pytex

contexts:
  main:
    - include: Packages/LaTeX/LaTeX.sublime-syntax
    - match: 🐍
      embed: Packages/Python/Python.sublime-syntax
      escape: 🐍
"""