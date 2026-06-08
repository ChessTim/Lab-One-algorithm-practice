def main():
    journal = {
        "Ivan": 78,
        "Anna": 92,
        "Maria": 85,
        "Petr": 55
    }
    
    while True:
        print("\nМеню:")
        print("1. Показать всех студентов")
        print("2. Добавить или обновить балл")
        print("3. Найти балл по имени")
        print("4. Найти студента с минимальным баллом")
        print("5. Выйти")
        
        choice = input("Выберите пункт: ")
        
        if choice == "1":
            print("\nСписок студентов:")
            for student in journal:
                print(student, "-", journal[student])
                
        elif choice == "2":
            name = input("Введите имя: ")
            score = int(input("Введите балл: "))
            journal[name] = score
            print("Сохранено")
                
        elif choice == "3":
            name = input("Введите имя для поиска: ")
            if name in journal:
                print("Балл:", journal[name])
            else:
                print("Студент не найден")
                
        elif choice == "4":
            min_student = ""
            min_score = 999
            
            for student in journal:
                if journal[student] < min_score:
                    min_score = journal[student]
                    min_student = student
            
            print("Минимальный балл у:", min_student, "(", min_score, ")")
            
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()