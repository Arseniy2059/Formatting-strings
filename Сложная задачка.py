first_team_name = "Мастера кода"
second_team_name = "Волшебники Данных"
first_team_count = 5
second_team_count = 6
first_team_time = 1552.512
second_team_time = 2153.31451
first_team_taks = 40
second_team_taks = 42

taks_total = first_team_taks + second_team_taks
time_total = first_team_time + second_team_time
time_avg = time_total / taks_total

if first_team_taks > second_team_taks or second_team_taks == first_team_taks and first_team_time > second_team_time:
    result = 'Победа команды Мастера кода!'
elif second_team_taks > first_team_taks and first_team_taks == second_team_taks or second_team_time > first_team_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = "Ничья!"

print('В команде %(name)s было %(count)d учасников.' % {'name': first_team_name, 'count': first_team_count})
print('Итога сегодня в командах учасников: %(first)x и %(second)x' % {'first': first_team_count, 'second': second_team_count})

print('Команда {} решила {} задач'.format(second_team_name, second_team_taks))
print('{} решила задач за {} с!'.format(first_team_name, second_team_time))

print(f'команды решили {taks_total} задач за {time_total} c!')
print(f'результат {result}')
