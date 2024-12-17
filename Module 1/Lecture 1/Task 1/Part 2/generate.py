import random
import json

# Данные для генерации
first_names = ["Иван", "Александр", "Михаил", "Дмитрий", "Андрей", "Сергей", "Николай", "Евгений", "Олег", "Павел"]
last_names = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков", "Фёдоров"]
patronymics = ["Алексеевич", "Иванович", "Сергеевич", "Дмитриевич", "Андреевич", "Николаевич", "Евгеньевич", "Олегович"]
specialties = ["Математика", "Физика", "ПМИ", "ПИ", "ИБ"]
grades_range = [2, 3, 4, 5]

# Генерация данных студентов
students = []

for _ in range(10):
    fio = f"{random.choice(last_names)} {random.choice(first_names)} {random.choice(patronymics)}"
    course = random.randint(1, 4)
    specialty = random.choice(specialties)
    grades = {
        "математика": random.choice(grades_range),
        "физика": random.choice(grades_range),
        "информатика": random.choice(grades_range),
    }
    students.append({
        "фио": fio,
        "курс": course,
        "специальность": specialty,
        "оценки": grades,
    })

# Сохранение данных в файл JSON
with open("students_data.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

print("Данные сохранены в файл students_data.json")
