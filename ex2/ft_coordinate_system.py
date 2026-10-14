import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        try:
            ask_data = input("Enter new coordinates as floats "
                             "in format 'x,y,z': ")
        except (KeyboardInterrupt, EOFError):
            print()
        else:
            temp_lst = []
            wrong_input = False
            for part in ask_data.split(","):
                try:
                    temp_lst.append(float(part))
                except ValueError:
                    wrong_input = True
            if wrong_input and temp_lst:
                raise ValueError(
                    f"Error on parameter '{ask_data}': could not convert"
                    f"string to float: '{ask_data}'"
                )
            if wrong_input or len(temp_lst) != 3:
                print("Invalid string")
                continue
            return tuple(temp_lst)


if __name__ == "__main__":
    while True:
        try:
            pos = get_player_pos()
            break
        except ValueError as e:
            print(e)
    print(f"Got a tuple: {pos}")
    x1 = pos[0]
    y1 = pos[1]
    z1 = pos[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Distance to center: {dist}")
    print()
    print("Get a second set of coordinates")
    while True:
        try:
            pos2 = get_player_pos()
            break
        except ValueError as e:
            print(e)
    x2 = pos2[0]
    y2 = pos2[1]
    z2 = pos2[2]
    dist2 = round(math.sqrt((x2-x1)**2
                  + (y2-y1)**2 + (z2-z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist2}")
