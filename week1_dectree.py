#решающие деревья, их обучение и нахождение наиболее важных признаков
import pandas as pd
import math
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/annagogley/Downloads/_ea07570741a3ec966e284208f588e50e_titanic.csv')
x = data[['Pclass','Fare','Age','Sex']]
y = data['Survived']
idint = data['PassengerId']
print(x)
for i in range(len(x.Pclass)):
    if math.isnan(x.Age[i]):
        x.Age[i] = 0
for i in range(len(x.Pclass)):
    if x.Sex[i] == 'female':
        x.Sex[i] = 0
    else:
        x.Sex[i] = 1
clf = DecisionTreeClassifier(random_state=241)
c = clf.fit(x, y)
importances = clf.feature_importances_
print(importances)
tree.plot_tree(c)
plt.show()

