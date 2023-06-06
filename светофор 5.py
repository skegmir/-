import turtle  # импорт черепахи

turtle.setup(400, 600)  # размер окна
wn = turtle.Screen()  # создание игровой площадки для черепахи
wn.title('светофор')  # заголовок
wn.bgcolor('skyblue')  # цвет фона окна
tess = turtle.Turtle()  # имя 1 черепахи
alex = turtle.Turtle()  # имя 2 черепахи
henry = turtle.Turtle()  # имя 3 черепахи


def draw_housing():
    """ Draw a nice housing to hold the traffic lights"""
    tess.pensize(3)  # ширина пера
    tess.color('black', 'white')  # цвет пера 
    tess.begin_fill()  # заливка
    tess.forward(80)  # перемещение
    tess.left(90)  # поворот
    tess.forward(200)
    tess.circle(40, 180)  # нарисовать полукруг
    tess.forward(200)
    tess.left(90)
    tess.end_fill()  # закончить закрашивание


draw_housing()


def circle(t, ht, colr):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()  # не рисовать
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')  # круг
    t.shapesize(3)  # размер круга
    t.fillcolor(colr)  # покрасить круг


circle(tess, 50, 'green')
circle(alex, 120, 'orange')
circle(henry, 190, 'red')
# переменная содержащая текущее состояние машины
state_num = 0


def advance_state_machine():
    """A state machine for traffic light"""
    global state_num  # НЕ создание новой переменной для state_num

    if state_num == 0:  # Переход из состояния 0 в состояние 1
        henry.color('darkgrey')
        alex.color('darkgrey')
        tess.color('green')
        wn.ontimer(advance_state_machine, 3000)  # таймер на 3 секунды
        state_num = 1
    elif state_num == 1:  # Переход из состояния 1 в состояние 2
        henry.color('darkgrey')
        alex.color('orange')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 2
    elif state_num == 2:  # Переход из состояния 2 в состояние 3
        tess.color('darkgrey')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 3
    else:                 # Переход из состояния 3 в состояние 0
        henry.color('red')
        alex.color('darkgrey')
        wn.ontimer(advance_state_machine, 2000)
        state_num = 0


advance_state_machine()
wn.listen()  # хз как это правильно назвать...дословно это "смотреть события"

wn.mainloop()  # ожидание пока юзер закроет окно черепахи