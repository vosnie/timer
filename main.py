Time = 0

def on_button_pressed_a():
    global Time
    while not (input.button_is_pressed(Button.B)):
        basic.pause(1000)
        Time += 1
        basic.show_number(Time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Time
    Time = 0
    basic.show_number(Time)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
