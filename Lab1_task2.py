from task_1 import  *   # TODO: импортируйте классы, созданные в ходе выполнения прошлого задани


cat1 = cat("Persik", 6, "Maine coon")
student1 = student("Volkov", 2, True)
prepod1 = prepod("Grishmanovsky", 138)

if __name__ == "__main__":

# TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
    # TODO: вызвать метод с некорректными аргументами(b)
        cat1.add_data(..., -1, ...)
    except:
        print('Ошибка: неправильные данные')

    try:
        student1.add_data(..., ..., 5)
     # TODO: вызвать метод с некорректными аргументами(a)
    except:
        print('Ошибка: неправильные данные')

    try:
        prepod1.add_data(..., -1)
     # TODO: вызвать метод с некорректными аргументами(a)
    except:
        print('Ошибка: неправильные данные')
