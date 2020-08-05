from turtle import Screen, Turtle

# --- constants ---

FONT = ("Arial", 60, "normal")

KEY_RESET = "r"
KEY_PAUSE = "p"
KEY_BOTH = "b"

# --- functions ---

def delSec(string):
    if len(string) == 1:
        return "0" + string

    return string

def tick():
    global milisecs, ticking

    turtle.clear()

    if milisecs < 0:
        turtle.write("TIMER DONE", align='center', font=FONT)
        screen.update()
        ticking = False
        return

    turtle.write( \
        delSec(str(milisecs // (60*60*10))) + ":" + \
        delSec(str((milisecs % (60*60*10)) // (60*10))) + ":" + \
        delSec(str((milisecs % (60*10)) // 10)) + "." + \
        str(milisecs % 10), align='center', font=FONT)

    screen.update()

    if not paused:
        milisecs -= 1

    screen.ontimer(tick, 100)

def reset():
    global milisecs, ticking

    print("reset")

    screen.onkey(None, KEY_RESET)  # Disable event handler inside handler
    screen.onkey(None, KEY_PAUSE)  # Disable event handler inside handler
    screen.onkey(None, KEY_BOTH)

    milisecs = sum(time*10)

    if not ticking:
        ticking = True
        tick()

    screen.onkey(reset, KEY_RESET)  # Reenable event handler
    screen.onkey(pause, KEY_PAUSE)  # Reenable event handler
    screen.onkey(both, KEY_BOTH)

def both():
    reset()
    pause()

def pause():
    global paused

    print("pause/unpause")

    paused = not paused

# --- main ---

strings = input("Please enter the time: ").strip().split(' ')

time = [60 ** (len(strings) - index - 1) * int(unit) for index, unit in enumerate(strings)]

milisecs = -1
ticking = False
paused = False

screen = Screen()
screen.bgcolor('darkblue')
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()
turtle.color('white')

reset()

screen.listen()
screen.mainloop()
