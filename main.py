# Dont worry about how this works, Just know it does
import os

def ShellSetUp():
  path = "/home/runner/CEasy/fdlr"
  os.system("clear")
  os.chdir(path)

def MkFile(x):
    sl = "clear && gcc {0}.c -o {0}.out && ./{0}.out && mv {0}.out exe".format(x)
    os.system(sl)
    
def main():
  ShellSetUp()
  print("Enter File Name :")
  UInput = input()
  MkFile(UInput)

main();