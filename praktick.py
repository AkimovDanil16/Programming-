users = {
    "student1" :{
        "password" :"1111",
     "grades": (12, 10, 8, 11, 9, 5, 4)
    },
     "student2" :{
         "password" :"2222",
        "grades":[8, 7, 11, 12, 10, 6, 11 ]
     },
     "student3" :{
 "password" :"3333",
    "grades":[7, 9, 7, 6, 5, 10, 11]
 },
 "student4" :{
     "password" :"4444",
     "grades":[12, 11, 10, 5, 7, 8, 9]
 }
}
login = input("Введіть логін:")
password = input("Введіть пароль:")
if login in users and users[login]["password"] == password:
    grades = users[login]["grades"]
    print("Вхід виконано успішно!")
    print("Ваші оцінки")
    for grade in grades:
        print(grade)
    satisfactory = 0
    unsatisfactory = 0
    for grade in grades:
            if 5<= grade <= 12:
                satisfactory += 1
            elif 1 <= grade  <=4:
                unsatisfactory += 1
    print("Кількість оцінок від 5 до 12:", satisfactory)
    print("Кількість оцінок від 1 до 4:", unsatisfactory)
else:
         print("Неправильний логін або пароль!")