def on_received_number(receivedNumber):
    music.set_volume(255)
    music.play(music.string_playable("F C F C F C F C ", 155),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.show_leds("""
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        . . . . .
        """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    music.stop_all_sounds()
    basic.show_leds("""
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    pass
radio.on_received_value(on_received_value)

basic.show_leds("""
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
