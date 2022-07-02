import json
import subprocess

command = input().split(' ')
mainCommand = command[0]
commandArgument = command[1]

jsonFilePath = './commands.json'
assistantCommands = json.load(open(jsonFilePath))

try:
    
    scriptPath = f'scripts/{ assistantCommands[mainCommand] }'
    
except KeyError: print('COMMAND IS SHIT')

subprocess.run(f'python { scriptPath } --file { commandArgument }', shell=True)