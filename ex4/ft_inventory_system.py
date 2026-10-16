import sys


def main() -> None:
    my_dict: dict[str, int] = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            key, value = arg.split(":", 1)
            if not key or not value:
                print(f"Error - invalid parameter '{arg}'")
                continue
            if key in my_dict.keys():
                print(f"Redundant item '{key}' - discarding")
                continue
            if (int(value) > 0):
                my_dict[key] = int(value)
            else:
                print(f"Invalid value {value}")
                continue
        except ValueError as error:
            print(f"Quantity error for '{key}': {error}")
    if my_dict == {}:
        print("Inventory is empty")
        return
    print(f"Got inventory: {my_dict}")
    print(f"Item list : {list(my_dict.keys())}")
    print(f"Total quantity of the {value} items: {sum(my_dict.values())}")
    for value in my_dict:
        percentage = ((my_dict[value]) / sum(my_dict.values())) * 100
        print(f"Item {value} represents {round(percentage,1)}%")

    min_key: str | None = None
    max_key: str | None = None
    print("teste", my_dict.items())
    for k, v in my_dict.items():
        if min_key is None or int(v) < my_dict[min_key]:
            min_key = k
        if max_key is None or int(v) > my_dict[max_key]:
            max_key = k
    print(f"Item most abundant: {max_key} with quantity"
          f"{my_dict[str(max_key)]}")
    print(f"Item least abundant: {min_key} with quantity"
          f"{my_dict[str(min_key)]}")
    print(f"Updated inventory : {my_dict}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
