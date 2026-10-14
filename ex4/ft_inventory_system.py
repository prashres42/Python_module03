import sys


def main():
    my_dict = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        
        try:
            key, value = arg.split(":", 1)
            if key in my_dict.keys():
                print(f"Redundant item '{key}' - discarding")
                continue
            my_dict[key] = int(value)
        except ValueError as error:
            print(f"Quantity error for '{key}': {error}")
        
    print(f"Got inventory: {my_dict}")

if __name__ == "__main__":
    main()