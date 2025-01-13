import getpass
from solvers import *
import os
import webbrowser
import time


# TODO: add all the things
# TODO: add arrow controls
# TODO: colours
# TODO: user manual

# COLOURS:
# reset: \x1b[0m
# text: light orange/yellow \x1b[38;5;227m (or \x1b[38;5;220m)
# lines: orange \x1b[38;5;208m
# selected item: green \x1b[38;5;40m
# error: red \x1b[38;5;160m

reset_colour = "\x1b[0m"
text_colours = ["\x1b[38;5;227m", "\x1b[38;5;220m"]
line_colour = "\x1b[38;5;172m"
selected_colour = "\x1b[38;5;40m"
error_colour = "\x1b[38;5;160m"


def open_user_manual():
    webbrowser.open("user_manual.pdf")

enter_is_pressed = False


problem_subchoices = {
    "polar coordinates and vectors": ["rectangular to polar", "polar to recangular", "vector addition"],
    "rectangular coordinates and points": ["distance between two points", "equation of a line through two points",
                                           "equation of a line through a point and perpendicular to another line"],
    "variations": ["direc variation", "indirect variation"],
    "abstract equations": ["find variable", "simplify fraction equation"],
    "roots": ["roots inside of roots"],
    "multi-equational/substitution": ["2 simulatenous equations", "advanced substition"],
    "volume concentration problems": [],
    "Combined gas law problems": ["Regular", "Constant Pressure", "Constant Volume", "Constant Temperature"],
    "30-60-90 triangles": [],
    "linear regression": ["y = mx + b"],
    "user manual": [],
    "exit": [],
}

for value in problem_subchoices.values():
    if value:
        value.append("go back")


problem_type_choices = list(problem_subchoices.keys())

# SOME OF THESE ARE STILL STRINGS, WHICH WILL CRASH WHEN CALLED (because you cant call a string obviously lol)
solver_funcs = {
    "polar coordinates and vectors": [cart_to_polar, polar_to_cart, vector_addition],
    "rectangular coordinates and points": [rect_distance, line_equation, line_equation_perpendicular],
    "variations": [],
    "abstract equations": [],
    "multi-equational/substitution": [],
    "volume concentration problems": [],
    "Combined gas law problems": [],
    "30-60-90 triangles": [],
    "linear regression": [],
    "user manual": [open_user_manual],
    "exit": [quit]
}

# displays choices box
def display_choices(choices):
    # TODO: make this prettier with ANSI escape codes and coloured text

    # get width of choices column
    max_length = max(len(choice) for choice in choices)
    # get width of number column
    count_length = len(str(len(choices) - 1))

    sides_str = "\x1b[38;5;214m+-" + "-" * count_length + "-+-" + "-" * max_length + "-+"

    # print top of choices box
    print(sides_str)
    for i in range(len(choices)):
        colour = text_colours[i % 2]
        # print and align options
        print(
            f"| {colour}{i:>{count_length}} {line_colour}| {colour}{choices[i]:<{max_length}} {line_colour}|")
    # print bottom of choices box
    print(sides_str + " \x1b[0m")


def get_choice(choices, message="Select choice: ", sentinel=(False, "exit")):
    # handle sentinel value
    if sentinel[0]:
        message += "(Type " + sentinel[1] + " to exit) "

    error = False
    prev_input = ""
    while True:

        # clear screen
        os.system("cls" if os.name == "nt" else "clear")

        # no choices
        if len(choices) == 0:
            return 0

        # error dialog
        error_message = f"Invalid input: {prev_input}. Input must be a number between 0 and {len(choices) - 1} (inclusive)"

        if error:
            print(error_message)

        # choice dialog
        print("\x1b[38;5;227m" + message + "\x1b[0m")
        display_choices(choices)
        choice = input("\x1b[38;5;40m> \x1b[0m")

        # handle sentinel value
        if sentinel[0] and choice == sentinel[1]:
            quit()

        # filter input until it is a choice
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(choices):
                raise IndexError
        except ValueError:
            pass
        except IndexError:
            pass
        else:
            return choice
        finally:
            prev_input = choice
            error = True

def main():
    while True:
        time.sleep(0.2)
        # get problem type
        choice = get_choice(problem_type_choices, "Select a problem type. Navigate with up or down arrow keys: ", [True, "exit"])

        # get specifc problem type
        subchoice = get_choice(problem_subchoices[problem_type_choices[choice]],
                               f"Select type of {problem_type_choices[choice]}: (Type .. to go back)")

        if subchoice == len(problem_type_choices) - 1 or subchoice == "..":
            continue

        # clear screen
        os.system("cls" if os.name == "nt" else "clear")

        # run correct solver function
        solver_funcs[problem_type_choices[choice]][subchoice]()


if __name__ == "__main__":
    main()