import turtle


def end_of_turtle():
    turtle.update()
    turtle.mainloop()


def fig(length, num, direction='right'):
    t = turtle.Turtle()
    t.speed(15)
    for i in range(0, num):
        t.forward(length)
        if direction == 'right' or direction == 'r':
            t.right(360 / num)
        else:
            t.left(360 / num)
    end_of_turtle()


def pattern_d(code, pattern, iterations):
    n = 1
    output_list = [code]
    while n + 1 <= iterations:
        new_line = ''
        output = output_list[-1]
        # print('Исходная строка: ', output)
        for ITEM_IND in range(len(output)):
            if output[ITEM_IND] == 'F' or output[ITEM_IND] == 'f':
                new_line += pattern
                # print('После добавления шаблона: ', new_line)
            else:
                new_line += output[ITEM_IND]
                # print('После добавления символа: ', new_line)
        output_list.append(new_line)
        n += 1
    output = output_list[-1]
    # print(output)
    return output


def fractal():
    simple_list = ['F--F--F', 10, 60, 'F+F--F+F', 4]
    what_to_do = []
    input_list = [
        'начальное условие', 'длину элемента', 'угол поворота', 'шаблон/правило', 'кол-во итераций'
    ]
    for ITEM in range(len(input_list)):
        what_to_do.append(input(f'Введите {input_list[ITEM]}: '))
    for ELEM in range(len(what_to_do)):
        if what_to_do[ELEM]:
            if what_to_do[ELEM].isdigit():
                what_to_do[ELEM] = int(what_to_do[ELEM])
        else:
            what_to_do[ELEM] = simple_list[ELEM]
    code = what_to_do[0]
    length = what_to_do[1]
    angle = what_to_do[2]
    pattern = what_to_do[3]
    iterations = what_to_do[4]

    script_line = pattern_d(code, pattern, iterations)

    t = turtle.Turtle()
    t.speed(45)

    for ELEM_IND in range(len(script_line)):
        if script_line[ELEM_IND] == 'F':
            t.forward(length)
        elif script_line[ELEM_IND] == '+':
            t.rt(angle)
        elif script_line[ELEM_IND] == '-':
            t.lt(angle)
        else:
            print('Input Error!')
            break

    end_of_turtle()


fractal()
