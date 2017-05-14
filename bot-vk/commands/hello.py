import command_system

def hello():
   message = "Привет, друг!\nЯ универсальный бот. Могу предложить тебе порцию мотивации, или свежий прогноз погоды.\nВоспользуйся 'инфо', что бы посмотреть мои возможности"
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'здорова', 'прив','что ты можешь?']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello