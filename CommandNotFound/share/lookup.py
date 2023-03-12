from chatgpt_wrapper import ChatGPT
import sys
import os
import tempfile




def main():
  cmd = ""
  args = []
  if len(sys.argv) < 2:
    exit(-1)
  cmd = sys.argv[1]
  if len(sys.argv) > 2:
    args = sys.argv[2:]

  bot = ChatGPT()
  arg_s = f"Write a bash script to implement the command {cmd}"
  if (len(args) > 0):
    arg_s = arg_s + " with INPUT variable"
  if (len(args) > 1):
    arg_s = arg_s + "s"

  for arg in args:
    arg_s = arg_s + " " + arg
  # print(arg_s)
  response = bot.ask(arg_s)
  # print(response)
  r = response[1]

  split = False
  if r.count("```") > 1:
    r = r.split("```")[1].split("```")[0].strip()
    split = True
  handle_file = False
  if split and '#!/bin/bash' in r:
    r = '#!/bin/bash'+r.split('#!/bin/bash')[1]
    handle_file = True
    # print("HANDLING BASH FILE")
    fp = tempfile.NamedTemporaryFile(suffix='.sh', delete=False)
    # print(r)
    fp.write(r.encode())
    fp.close()
    os.system(f"chmod +x {fp.name}")
    c = fp.name
    for arg in args:
      c = c + " " + arg
    os.system(c)
    # os.remove(fp.name)

  inc = True
  for arg in args:
    if arg not in r:
      inc = False
  if (not handle_file) and split and inc:
    # print("HANDLING SH COMMAND")
    # print(r)
    os.system(f"eval {r}")

  

if __name__ == "__main__":
  main()
