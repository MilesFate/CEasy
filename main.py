# Dont worry about how this works, Just know it does
import os

# changes directory and clears terminal
def ShellSetUp():
  path = "/home/runner/CEasy/fdlr" # change this to fit your needs
  os.system("clear")
  os.chdir(path)

# the main functionality of this script
def MkFile(x):
    sl = "clear && gcc {0}.c -o {0}.out && ./{0}.out && mv {0}.out exe".format(x)
    os.system(sl)

# gets the user input and runs the code
def main():
  ShellSetUp()
  print("Enter File Name :")
  UInput = input()
  MkFile(UInput)

if __name__ == "__main__":
  main()