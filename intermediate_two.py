usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Enter your username\n\n>>>")
check = False
for name in usernames:
    if name == user_name:
        check = True

if check == True:
    print("Access granted")
else:
    print("Access denied")
