#предобработка данных в пандас на основе данных пассажиров Титаника
import pandas as pd
import math

data = pd.read_csv('/Users/annagogley/Downloads/_ea07570741a3ec966e284208f588e50e_titanic.csv')

# подсчет количества мужчин и женщин.
# Знаю, что можно было использовать data['Sex'].value_counts(), но захотелось реализовать через цикл.
male = 0
female = 0
for i in range(len(data['Sex'])):
    if data.Sex[i] == 'male':
        male += 1
    else:
        female += 1
print('мужчин на борту', male, 'женщин на борту', female)

#процент выживщих на борту
surv = 0
dead = 0
for i in range(len(data.Survived)):
    if data.Survived[i] == 0:
        dead += 1
    else:
        surv += 1
print('Доля выживших составляла(%):', surv/((surv + dead)/100))

#процент пассажиров первого класса на борту
class1 = 0
class2 = 0
class3 = 0
for i in range(len(data.Pclass)):
    if data.Pclass[i] == 1:
        class1 += 1
    elif data.Pclass[i] == 2:
        class2 += 1
    else:
        class3 += 1
print('Доля пассажиров первого класса составляла(%):', class1/((class2 + class3 + class1)/100))

#подсчет среднего и медианного возраста.
total_age = 0
age = []
for i in range(len(data.Age)):
    if math.isnan(data.Age[i]) is False:
        total_age += data.Age[i]
        age.append(data.Age[i])
    else:
        total_age += 0
print('srednii vosrast:', total_age/len(data.Age))
#bubble sort
for i in range(len(age) - 1):
    for j in range(len(age) - i - 1):
        if age[j] > age[j+1]:
            age[j+1], age[j] = age[j], age[j+1]
med = 0
if len(age) % 2 == 0:
    med = age[len(age) // 2]
else:
    med = (age[len(age) // 2 + 1] + age[len(age) // 2]) / 2
print('mediannii vozrast:', med)

#подсчет корреляции Пирсона между числом братьев/сестер/супруг и числом родителей/детей
print(data[['SibSp','Parch']].corr(method='pearson'))

#поиск самого часто встречающегося женского имени на корабле
fem_name = []
for i in range(len(data.Sex)):
    if data.Sex[i] == 'female':
        fem_name.append(data.Name[i])
names = []
for i in range(len(fem_name)):
    temp = fem_name[i].split(',')
    if 'Miss.' in temp[1]:
        temp2 = temp[1].split(' ')
        names.append(temp2[2])
    else:
        if '(' in temp[1]:
            temp3 = temp[1].split('(')
            temp4 = temp3[1].split(' ')
            names.append(temp4[0])
        else:
            temp3 = temp[1].split(' ')
            names.append(temp3[2])
print(names)

dict_names = []
K = []
for i in range(len(names)):
    k = 0
    for j in range(len(names)):
        if names[i] in names[j]:
            k += 1
    dict_names.append(names[i])
    K.append(k)

print(dict_names)
print(K)
df = pd.DataFrame(list(zip(dict_names, K)), columns = ['Name', 'val'])
print(df)
max = 0
Max = []
for i in range(len(df.val)):
    if df.val[i] > max:
        max = df.val[i]
for i in range(len(df.val)):
    if df.val[i] == max:
        print(df.Name[i], max)