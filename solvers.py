import getpass
import numpy as np

error_number_msg = "Invalid input. Input must be a number"
error_pair_msg = "Invalid input. Input must be an x, y pair"
error_bool_msg = "Invalid input. Input must be a boolean (True or False)"

RAD2DEG = 180 / np.pi


# root is an int (whats in the root)
# returns whatever is in the root and the factor
# example: simplify_root(18) -> (3, 2) -> 3√2
def simplify_root(root):
    outside = 1
    inside = root
    factor = 2
    while inside > factor:
        if inside % (factor * factor) == 0:
            outside *= factor
            inside //= factor * factor
        else:
            factor += 1
    return outside, inside


class Root:

    def __init__(self, inside, outside):
        self.outside, self.inside = simplify_root(inside * outside * outside)
        self.outside = ifint(self.outside)
        self.inside = ifint(self.inside)

    def __str__(self):
        outside_str = "" if self.outside == 1 else self.outside
        return f"{outside_str}√{self.inside}"


# utitilies


def ifint(x):
    if isinstance(x, float):
        return int(x) if x.is_integer() else x
    return x


def wait():
    getpass.getpass("\nPress enter to continue...")


def get_num(msg="", err_msg="Invaild input"):
    error = False
    while True:
        if error:
            print(err_msg)
        inp = input(msg)

        try:
            inp = float(inp)
        except ValueError:
            error = True
        else:
            return ifint(inp)


def get_pair(msg="", err_msg="Invaild input"):
    error = False
    while True:
        if error:
            print("\x1b[A\r\x1b[A\r" + err_msg)

        inp = input(msg)
        inp.replace(" ", "")
        inp.replace("(", "")
        inp.replace(")", "")

        try:
            inp1 = float(inp.split(",")[0])
            inp2 = float(inp.split(",")[1])
        except ValueError:
            error = True
        except IndexError:
            error = True
        else:
            return ifint(inp1), ifint(inp2)


def get_bool(msg="", err_msg="Invaild input"):
    error = False
    while True:
        if error:
            print("\x1b[A\r\x1b[A\r" + err_msg)

        inp = input(msg)

        if inp.lower() == "true":
            return True
        elif inp.lower() == "false":
            return False
        else:
            error = True


def working():
    print("\n" + "-" * 12 + "[ WORKING ]" + "-" * 13 + "\n")


def answer():
    print("\n" + "-" * 10 + "[ FINAL ANSWER ]" + "-" * 10 + "\n")


def cart_to_polar():
    x = get_num("X or R value: ", error_number_msg)
    y = get_num("Y or U value: ", error_number_msg)

    working()

    r = round(np.sqrt(x * x + y * y), 3)
    r = ifint(r)

    # radius
    print(f"r = √({x}² + {y}²)")
    print(f"r = √({x * x} + {y * y})")
    print(f"r = √{x * x + y * y}")
    print(f"r = {r}\n")
    # figure this out
    theta = 0

    rho = RAD2DEG * np.arctan(abs(y) / abs(x))

    print(f"ρ = tan⁻¹({abs(y)} / {abs(x)})")
    print(f"ρ = {round(np.arctan(abs(y) / abs(x)), 3)}\n")

    # Q1
    if x > 0 and y > 0:
        theta = rho
        print("We are in Q1, so θ = ρ")

    # Q2
    if x < 0 and y > 0:
        theta = 180 - rho
        print("We are in Q2, so θ = 180 - ρ")

    # Q3
    if x < 0 and y < 0:
        theta = 180 + rho
        print("We are in Q3, so θ = 180 + ρ")

    # Q4
    if x > 0 and y < 0:
        theta = 360 - rho
        print("We are in Q4, so θ = 360 - ρ")

    theta = ifint(round(theta, 3))
    print(f"θ = {theta}")

    answer()

    # form and answer
    print(f"r∠ θ")
    print(f"{r}∠ {theta}°")

    wait()


def polar_to_cart():
    r = get_num("r value: ", error_number_msg)
    theta = get_num("θ value (degrees): ", error_number_msg)

    working()

    print(f"x = r * cos(θ)")
    print(f"y = r * sin(θ)\n")

    print(f"x = {r} * cos({theta}°)")
    print(f"y = {r} * sin({theta}°)\n")

    x = round(r * np.cos(np.deg2rad(theta)), 3)
    y = round(r * np.sin(np.deg2rad(theta)), 3)

    x = ifint(x)
    y = ifint(y)

    print(f"x = {x}")
    print(f"y = {y}")

    answer()
    sign = "-" if y < 0 else "+"
    print("xî + yĵ")
    print(f"{x}î {sign} {abs(y)}ĵ")

    wait()


def vector_addition():
    r1 = get_num("First r value: ", error_number_msg)
    theta1 = get_num("First θ value (degrees): ", error_number_msg)

    r2 = get_num("Second r value: ", error_number_msg)
    theta2 = get_num("Second θ value (degrees): ", error_number_msg)

    cartesian = get_bool(
        "Should the output be in rectangular coordinates? (True or False): ",
        error_bool_msg)

    working()

    print(f"v₁ = r₁ * cos(θ₁), r₁ * sin(θ₁)")
    print(f"v₂ = r₂ * cos(θ₂), r₂ * sin(θ₂)\n")

    print(f"v₁ = {r1} * cos({theta1}°), {r1} * sin({theta1}°)")
    print(f"v₂ = {r2} * cos({theta2}°), {r2} * sin({theta2}°)\n")

    x1 = round(r1 * np.cos(np.deg2rad(theta1)), 3)
    y1 = round(r1 * np.sin(np.deg2rad(theta1)), 3)
    x2 = round(r2 * np.cos(np.deg2rad(theta2)), 3)
    y2 = round(r2 * np.sin(np.deg2rad(theta2)), 3)

    # round these too because floating point precision errors
    xf = round(x1 + x2, 3)
    yf = round(y1 + y2, 3)

    length = max(len(f"v₁ = {x1}, {abs(y1)}"), len(f"v₂ = {x2}, {abs(y2)}"))

    print(f"v₁ = {x1}, {y1}")
    print(f"v₂ = {x2}, {y2} + \n     " + "-" * length + "\n")

    print(f"vf = {xf}, {yf}")

    if not cartesian:
        # vf = num1, num2
        r = round(np.sqrt(xf * xf + yf * yf), 6)
        r = ifint(r)

        # radius
        print(f"\nr = √({xf}² + {yf}²)")
        print(f"r = √({round(xf * xf, 6)} + {round(yf * yf, 6)})")
        print(f"r = √{r}")
        print(f"r = {np.sqrt(r)}\n")
        theta = 0

        rho = RAD2DEG * np.arctan(abs(yf) / abs(xf))

        print(f"ρ = tan⁻¹({abs(yf)} / {abs(xf)})")
        print(f"ρ = {round(np.arctan(abs(yf) / abs(xf)), 3)}\n")

        # Q1
        if xf > 0 and yf > 0:
            theta = rho
            print("We are in Q1, so θ = ρ")

        # Q2
        if xf < 0 and yf > 0:
            theta = 180 - rho
            print("We are in Q2, so θ = 180 - ρ")

        # Q3
        if xf < 0 and yf < 0:
            theta = 180 + rho
            print("We are in Q3, so θ = 180 + ρ")

        # Q4
        if xf > 0 and yf < 0:
            theta = 360 - rho
            print("We are in Q4, so θ = 360 - ρ")

        theta = ifint(round(theta, 3))
        print(f"θ = {theta}")

        answer()

        # form and answer
        print(f"r∠ θ")
        print(f"{round(r, 3)}∠ {theta}°")
        pass

    else:
        answer()

        sign = "-" if yf < 0 else "+"
        print("xî + yĵ")
        print(f"{round(xf, 3)}î {sign} {round(abs(yf), 3)}ĵ")

    wait()


def rect_distance():
    x1, y1 = get_pair("First coordinate point: ", error_pair_msg)
    x2, y2 = get_pair("Second coordinate point: ", error_pair_msg)

    raw_dist = (x1 - x2)**2 + (y1 - y2)**2

    working()

    print(f"d = √((x₁ - x₂)² + (y₁ - y₂)²)")
    print(f"d = √(({x1} - {x2})² + ({y1} - {y2})²)")
    print(f"d = √({x1 - x2}² + {y1 - y2}²)")
    print(f"d = √({(x1 - x2) ** 2} + {(y1 - y2) ** 2})")
    print(f"d = √{raw_dist}")
    answer()
    print(f"d = {Root(raw_dist, 1)}\n")

    wait()


def line_equation():
    x1, y1 = get_pair("First coordinate point: ", error_pair_msg)
    x2, y2 = get_pair("Second coordinate point: ", error_pair_msg)

    working()

    print("m = (y₂ - y₁) / (x₂ - x₁)")
    print(f"m = ({y2} - {y1}) / ({x2} - {x1})")
    print(f"m = {y2 - y1} / {x2 - x1}")

    n = y2 - y1
    d = x2 - x1

    print(f"y = {n} / {d} x + b")


    # m = y2 - y1 / x2 - x1


def line_equation_perpendicular():
    pass


def tsn_trinagles():
    c = get_num("Hypotenuse side measurement (type u for unknown): ",
                error_number_msg)

    b = get_num("Longer side measurement (type u for unknown): ",
                error_number_msg)

    a = get_num("Shorter side measurement (type u for unknown): ",
                error_number_msg)

    working()


"""
right triangle:

    .
   /|
:c/ | b:
 /  |
∠___⅃
  a
"""
