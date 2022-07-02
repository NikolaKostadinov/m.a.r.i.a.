import argparse
import os

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
        if file in files:
            os.startfile(os.path.join(root, file))