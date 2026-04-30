radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 5) {
        music.setVolume(255)
        music.play(music.stringPlayable("F C F C F C F C ", 155), music.PlaybackMode.LoopingInBackground)
        basic.showLeds(`
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.A, function () {
    music.stopAllSounds()
    basic.showLeds(`
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        `)
})
radio.setGroup(1)
basic.showLeds(`
    . # # # .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    `)
