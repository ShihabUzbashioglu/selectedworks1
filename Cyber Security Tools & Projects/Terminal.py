from subprocess import run
from os import system

system('clear') # cls screen

while True:

    command = input("Enter Command :")
    if command.lower = "exit":
        exit()
    try:
        run(command)
    except:
        print(f'{command} :command isnt found or defined')

