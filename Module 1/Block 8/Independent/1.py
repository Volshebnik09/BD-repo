import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')

def plot_survival_count():
    plt.figure(figsize=(8, 5))
    sns.countplot(data=data, x='survived', palette='Set2')
    plt.title('Количество выживших и погибших пассажиров', fontsize=16)
    plt.xlabel('Выжил (0 - нет, 1 - да)', fontsize=12)
    plt.ylabel('Количество пассажиров', fontsize=12)
    plt.xticks([0, 1], ['Погибшие', 'Выжившие'])
    plt.show()

def plot_age_distribution():
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='age', hue='survived', multiple='stack', bins=30, palette='coolwarm')
    plt.title('Распределение возраста у выживших и погибших пассажиров', fontsize=16)
    plt.xlabel('Возраст', fontsize=12)
    plt.ylabel('Количество пассажиров', fontsize=12)
    plt.legend(['Погибшие', 'Выжившие'])
    plt.show()

def plot_survival_by_class_and_sex():
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x='pclass', y='survived', hue='sex', palette='Set1')
    plt.title('Выживаемость пассажиров в зависимости от класса и пола', fontsize=16)
    plt.xlabel('Класс пассажира', fontsize=12)
    plt.ylabel('Доля выживших', fontsize=12)
    plt.xticks([0, 1, 2], ['Первый класс', 'Второй класс', 'Третий класс'])
    plt.legend(title='Пол')
    plt.show()

plot_survival_count()
plot_age_distribution()
plot_survival_by_class_and_sex()