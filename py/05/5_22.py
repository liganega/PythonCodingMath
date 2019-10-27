import pandas as pd

team_list = df.set_index('Team').index
print (team_list)

team = []
for i in team_list:
    if i not in team:
        team.append(i)
team

team_summary = {}
for i in range(len(team)):
    team_summary[team[i]] = df.set_index('Team').loc[team[i]].mean()
    
print (team_summary['Korea Republic'])
print ('')


print (team_summary['France'])
print ('')

print (team_summary['Korea Republic'][13])
print ('')
fouls = {}
goals = {}
possession = {}
distance = {}
yellow_and_red = {}
pass_accuracy = {}

for i in range(len(team)):
    fouls[team[i]] = team_summary[team[i]][13]   
    goals[team[i]] = team_summary[team[i]][0]    
    possession[team[i]] = team_summary[team[i]][1]  
    pass_accuracy[team[i]] = team_summary[team[i]][9]    
    distance[team[i]] = team_summary[team[i]][11]    
    yellow_and_red[team[i]] = team_summary[team[i]][15]    

print (fouls)
print (max(fouls, key=fouls.get))
print ('')
print ('가장 골 많이 넣은 나라 : {}'.format(max(goals, key=goals.get)))
print ('가장 점유율 높은 나라 : {}'.format(max(possession, key=possession.get)))
print ('가장 패스 정확도 높은 나라 : {}'.format(max(pass_accuracy, key=pass_accuracy.get)))
print ('가장 뛴 거리가 많은 나라 : {}'.format(max(distance, key=distance.get)))
print ('가장 경고 & 퇴장 많이 받은 나라 : {}'.format(max(yellow_and_red, key=yellow_and_red.get)))

score = {}
for i in range(len(team)):
    score[team[i]] = team_summary[team[i]][0]*2 + team_summary[team[i]][1]*0.1 + team_summary[team[i]][9]*0.15 \
                     + team_summary[team[i]][11]*0.005 - team_summary[team[i]][15]

print (score)
print ('')
print ('가장 아름다운 축구를 한 나라 : {}'.format(max(score, key=score.get)))
print ('가장 안 아름다운 축구를 한 나라 : {}'.format(min(score, key=score.get)))