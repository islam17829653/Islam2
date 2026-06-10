import json
import os

FILE_NAME = "students.json"


# Файлдан оқу
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


# Файлға сақтау
def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# Студент қосу
def add_student(students):
    while True:
        name = input("Аты-жөні: ").strip()
        if name:
            break
        print("Қате! Аты бос болмауы керек.")

    while True:
        try:
            age = int(input("Жасы: "))
            if age > 0:
                break
            print("Қате! Жас теріс немесе 0 болмауы керек.")
        except ValueError:
            print("Қате! Сан енгізіңіз.")

    while True:
        try:
            grade = float(input("Бағасы: "))
            if 0 <= grade <= 100:
                break
            print("Қате! Баға 0-100 аралығында болуы керек.")
        except ValueError:
            print("Қате! Сан енгізіңіз.")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    save_students(students)
    print("Студент сәтті қосылды!")


# Студенттер тізімі
def show_students(students):
    if not students:
        print("Студенттер тізімі бос.")
        return

    print("\n===== Студенттер тізімі =====")
    for i, student in enumerate(students, start=1):
        print(
            f"{i}. {student['name']} | Жасы: {student['age']} | Бағасы: {student['grade']}"
        )


# Статистика
def show_statistics(students):
    if not students:
        print("Статистика үшін мәлімет жоқ.")
        return

    total_students = len(students)
    average_grade = sum(student["grade"] for student in students) / total_students
    best_student = max(students, key=lambda x: x["grade"])

    print("\n===== Статистика =====")
    print(f"Студенттер саны: {total_students}")
    print(f"Орташа баға: {average_grade:.1f}")
    print("Ең жоғары баға:")
    print(f"{best_student['name']} - {best_student['grade']}")


# Негізгі бағдарлама
def main():
    students = load_students()

    while True:
        print("\n===== Студенттер базасы =====")
        print("1. Студент қосу")
        print("2. Студенттер тізімін көру")
        print("3. Статистика")
        print("0. Шығу")

        choice = input("Таңдауыңыз: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_statistics(students)
        elif choice == "0":
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате! Дұрыс таңдау енгізіңіз.")


if __name__ == "__main__":
    main()