import os
import shutil
import time

os.system("@echo off & title Builder - Loading... & cd C:/projects/server/Server & color 0c")
print("\nLoading...")

if os.path.isdir("build"):
    shutil.rmtree("build")
os.mkdir("build")
os.chdir("build")
time.sleep(1.3)

print("\nBuilding...\n")
os.system("title Builder - Building... & color 06 & pyinstaller ../server/main.py -i ../server/icon.ico --hidden-import=json")

time.sleep(0.3)
os.system("title Builder - Cleaning & color 02")
print("\nCleaning...")

os.remove("main.spec")
shutil.rmtree("build")
os.chdir("dist/main")
os.system("ren main.exe Server.exe")

time.sleep(2.1)

os.system("title Builder - Finished! & color 0a")
print("\nDone! You can close this window now!")
input()
