team_name1 = 'Мастера кода'
team_name2 = 'Волшебники данных'
team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team_name1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team_name2}!'
else:
    challenge_result = 'Ничья!'


print('В команде %s участников: %s!' % (team_name1, team1_num))
print('В команде %s участников: %s!' % (team_name2, team2_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

print("Команда {} решила задач: {}!".format(team_name1, score_1))
print("Команда {} решила задач: {}!".format(team_name2, score_2))
print("Команда {} решили задачи за {} с!".format(team_name1, team1_time))
print("Команда {} решили задачи за {} с !".format(team_name1, team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')
