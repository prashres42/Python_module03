import sys


def main():
    my_dict = {}
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
            my_dict[key] = int(value)
        except ValueError as error:
            print(f"Quantity error for '{key}': {error}")
    if my_dict == {}:
        print("Inventory is empty")
        return

    if sum(my_dict.values()) > 0:
        print(f"Got inventory: {my_dict}")
        print(f"Item list : {list(my_dict.keys())}")
        print(f"Total quantity of the {value} items: {sum(my_dict.values())}")
        for value in my_dict:
            percentage = ((my_dict[value]) / sum(my_dict.values())) * 100
            print(f"Item {key} represents {round(percentage,1)}%")

        min_key = max_key = None

        for key, value in my_dict.items():
            if min_key is None or value < my_dict[min_key]:
                min_key = key
            if max_key is None or value > my_dict[max_key]:
                max_key = key
        print(f"Item most abundant: {max_key} with quantity {my_dict[max_key]}")
        print(f"Item least abundant: {min_key} with quantity {my_dict[min_key]}")
        print(f"Updated inventory : {my_dict}")
    else:
        print("Invalid values introduced")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
