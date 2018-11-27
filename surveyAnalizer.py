import matplotlib.pyplot as plt

usersCount = 0
answers = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0]]

with open('./dataset/survey_answers.txt') as f:
  for line in f:
    usersCount += 1
    values = line.split()
    n = 0
    for v in values:
      answers[n][int(v)-1] += 1
      n += 1

c = 0
for q in answers:
  answers[c] = [str(round(100*i/usersCount,2))+' %' for i in answers[c]]
  c += 1

print('Frecuencia de calificación reportada por usuarios según nivel de preferencia')
print(answers)

surveyRatingsCount = 0
surveyRatings = [0,0,0,0,0]
with open('./dataset/test.txt') as f:
  for line in f:
    surveyRatings[int(line.split()[2])-1] += 1
    surveyRatingsCount += 1
  
surveyRatings = [round(i/surveyRatingsCount,4) for i in surveyRatings]
print(surveyRatings)

baseRatingsCount = 0
baseRatings = [0,0,0,0,0]
with open('./dataset/train.txt') as f:
  for line in f:
    baseRatings[int(line.split()[2])-1] += 1
    baseRatingsCount += 1
    if baseRatingsCount == surveyRatingsCount:
      break
  
baseRatings = [round(i/baseRatingsCount,4) for i in baseRatings]
print(baseRatings)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.bar(x = [1,2,3,4,5], height=baseRatings)
ax1.set_title('Base ratings')
ax2.bar(x = [1,2,3,4,5], height=surveyRatings)
ax2.set_title('Survey ratings')
plt.show()
