import argparse
from operator import contains
import os

from matplotlib.pyplot import bar_label

parser = argparse.ArgumentParser(description='Open file')
parser.add_argument(
                    '-f',
                    '--file',
                    type=str,
                    help='set path of file to open'
                )
args = parser.parse_args()
file = args.file

homeDir = os.path.expanduser('~')
for root, dirs, files in os.walk(homeDir):
    
    for fullFileName in files:
        
        fileName = fullFileName.split('.')[0]
        
        if file == fileName:
            filePath = os.path.join(root, fullFileName)
            os.startfile(filePath)
            break