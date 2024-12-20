from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene

# Function to display the intro graphics
def intro_graphics(screen):
    effects = [
        Cycle(
            screen,
            FigletText("WELCOME TO HILLES GAME", font='big'),
            int(screen.height / 2 - 4)
        ),
        Cycle(
            screen,
            FigletText("Press space bar to continue", font='small'),
            int(screen.height / 1.2 - 4)
        ),
        Stars(screen, 200)
    ]

    # Play the animation
    screen.play([Scene(effects, 200)], stop_on_resize=True, repeat=False)

    # Wait for a key press after the animation
    while True:
        key = screen.get_key()
        if key:  # Proceed if any key is pressed
            break
    # Clear the screen after the intro
    screen.clear()


def outro_graphics(screen):
    effects = [
        Cycle(
            screen,
            FigletText("GAME OVER", font='big'),
            int(screen.height / 2 - 4)
        ),
        Cycle(
            screen,
            FigletText("Congratulations", font='small'),
            int(screen.height / 1.3 - 4),
        ),
        Cycle(
            screen,
            FigletText("you made it back to Bryn Mawr!", font='small'),
            int(screen.height / 1.1 - 4)
        ),
        Stars(screen, 200)
    ]

    # Play the animation
    screen.play([Scene(effects, 200)], stop_on_resize=True, repeat=False)

    while True:
        key = screen.get_key()
        if key:  # Proceed if any key is pressed
            break

    screen.clear()




