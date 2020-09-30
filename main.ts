let Time = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    while (!input.buttonIsPressed(Button.B)) {
        basic.pause(1000)
        Time += 1
        basic.showNumber(Time)
    }
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Time = 0
    basic.showNumber(Time)
})
