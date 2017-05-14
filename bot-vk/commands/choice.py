import command_system
from random import randint

def choice():
    if randint(1,2) == 1:
        message = 'Ответ - Да.'
    else:
        message = 'Ответ - Нет.'
    return message, ''

choice_command = command_system.Command()

choice_command.keys = ['выбор','мне идти на пару?','помоги решить','да или нет', 'да/нет']
choice_command.description = 'Помогу сделать выбор - Да/Нет'
choice_command.process = choice