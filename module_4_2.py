def test_function():
    sent = 'Я в области видимости функции test_function'
    def inner_function():
        nonlocal sent
        sent += '. Ой, уже нет!'
        print(sent)

    print(sent)

    inner_function()

    print(sent)

    def inner_function2():
        sent = ''
        sent += 'Я - вторая встроенная функция!'
        print(sent)

    inner_function2()
    print(sent)


test_function()

inner_function2()