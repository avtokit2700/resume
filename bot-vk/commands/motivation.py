import command_system
import vkapi

def motivation_fitness():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-44131843)
   message = 'Вот тебе порция мотивахи фитнеса, брат'
   return message, attachment

motivation_fitness_command = command_system.Command()

motivation_fitness_command.keys = ['мотивация фитнеса', 'фитнес', 'качалка']
motivation_fitness_command.description = 'Пришлю мотивацию фитнеса'
motivation_fitness_command.process = motivation_fitness

#-100083164

def motivation():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-100083164)
   message = 'Вот тебе порция мотивахи успеха, брат'
   return message, attachment

motivation_command = command_system.Command()

motivation_command.keys = ['мотивация успеха', 'успех', 'мотивашка']
motivation_command.description = 'Пришлю мотивацию для успеха'
motivation_command.process = motivation