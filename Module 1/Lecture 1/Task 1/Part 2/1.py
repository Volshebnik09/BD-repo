import json
from collections import defaultdict

file_path = "./students_data.json"

with open(file_path, 'r', encoding='utf-8') as file:
    students = json.load(file)

subject_scores = {}
subject_counts = {}

for student in students:
    for subject, grade in student['оценки'].items():
        if subject not in subject_scores:
            subject_scores[subject] = 0
            subject_counts[subject] = 0
        subject_scores[subject] += grade
        subject_counts[subject] += 1

subject_averages = {
    subject: subject_scores[subject] / subject_counts[subject]
    for subject in subject_scores
}

max_average = max(subject_averages.values())

best_subjects = [
    subject for subject, avg in subject_averages.items() if avg == max_average
]

specialty_count = defaultdict(int)

for student in students:
    specialty_count[student['специальность']] += 1

specialties_with_few_students = [
    specialty for specialty, count in specialty_count.items() if count < 2
]

course_scores = defaultdict(int)
course_counts = defaultdict(int)

for student in students:
    course = student['курс']
    # Для каждого предмета в оценках студента добавляем оценку к сумме для курса
    total_grade = sum(student['оценки'].values())
    course_scores[course] += total_grade
    course_counts[course] += len(student['оценки'])  # Добавляем количество предметов

course_averages = {
    course: course_scores[course] / course_counts[course]
    for course in course_scores
}

max_average = max(course_averages.values())

best_courses = [
    course for course, avg in course_averages.items() if avg == max_average
]
print("ФИО (Фамилии) тех, у кого среди оценок только 4 или 5:")
print([
    student['фио'].split()[0]
    for student in students
    if all(grade >= 4 for grade in student['оценки'].values())
])
print("ФИО (Фамилии) тех, у кого среди оценок есть хотя бы одна 2:")
print([
    student['фио'].split()[0]
    for student in students
    if any(grade == 2 for grade in student['оценки'].values())
])
print("Предметы, которые сданы лучше других по итогам сессии:", best_subjects)
print("Специальности, у студентов которых меньше 2:", specialties_with_few_students)
print("Курсы, студенты которых лучше сдали сессию:", best_courses)