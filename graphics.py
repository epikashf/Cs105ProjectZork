# from asciimatics.screen import Screen
# from asciimatics.effects import Cycle, Stars
# from asciimatics.renderers import FigletText
# from asciimatics.scene import Scene
#
#
# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("ASCIIMATICS", font='big'),
#             int(screen.height / 2 - 8)),
#         Cycle(
#             screen,
#             FigletText("ROCKS!", font='big'),
#             int(screen.height / 2 + 3)),
#         Stars(screen, 200)
#     ]
#
#     # Play the animation for 500 frames (or adjust as needed)
#     screen.play([Scene(effects, 500)])
#
#     # Refresh the screen to make sure everything is rendered
#     screen.refresh()
#
#     # Wait for the user to press any key after the animation
#     screen.get_key()
#
#     # Clear the screen and start the game
#     screen.clear()
#
#
#     # Now, start the game loop
#
#
# # Start the screen and call the demo function
# Screen.wrapper(demo)

