from datetime import datetime

# Атын енгізу
while True:
    name = input("Атыңыз: ").strip()
    if name == "":
        print("Қате! Аты бос болмауы керек.")
    else:
        break

# Жасты енгізу
while True:
    age = input("Жасыңыз: ")

    if not age.isdigit():
        print("Қате! Жас тек сан болуы керек.")
        continue

    age = int(age)

    if age < 0:
        print("Қате! Жас теріс болмауы керек.")
    else:
        break

# Қаланы енгізу
city = input("Қалаңыз: ")

# Экранға шығару
print("\n===== Пайдаланушы мәліметтері =====")
print("Аты:", name)
print("Жасы:", age)
print("Қаласы:", city)

# Күн мен уақыт
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Лог файлға жазу
with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"[{current_time}]\n")
    file.write("Пайдаланушы тіркелді\n")
    file.write(f"Аты: {name}\n")
    file.write(f"Жасы: {age}\n")
    file.write(f"Қаласы: {city}\n")
    file.write("-" * 30 + "\n")

print("\nДеректер log.txt файлына сақталды.")

# ===== Статистика =====
count = 0
last_user = ""
last_time = ""

with open("log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i in range(len(lines)):
    if "Пайдаланушы тіркелді" in lines[i]:
        count += 1

    if lines[i].startswith("["):
        last_time = lines[i].strip("[]\n")

    if lines[i].startswith("Аты:"):
        last_user = lines[i].replace("Аты:", "").strip()

print("\n===== Статистика =====")
print("Тіркелген пайдаланушылар саны:", count)
print("Соңғы пайдаланушы:")
print("Аты:", last_user)
print("Соңғы әрекет:")
print(last_time)