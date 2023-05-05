import os
import sys

# Iterate through this folder, and delete all folders labelled 1_files, 2_files etc.
def main():
    for folder in os.listdir():
        if folder.endswith('_files'):
            os.system('rm -rf ' + folder)

if __name__ == '__main__':
    #main()
    print("Not executed.")
    