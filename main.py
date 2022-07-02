import json
import subprocess
import os

# Get Input
command = input().split(' ')
mainCommand = command[0]
commandArgument = command[1]

# Open Commands JSON
jsonFilePath = './commands.json'
assistantCommands = json.load(open(jsonFilePath))

# Run Script
try:
    
    scriptPath = f'scripts/{ assistantCommands[mainCommand] }'
    
except KeyError: raise('COMMAND IS NOT DEFINED')

subprocess.run(f'python { scriptPath } --file { commandArgument }', shell=True)