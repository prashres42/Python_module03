import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name : {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No Argument provided!")
    else:
        print(f"Arguments received : {len(sys.argv[1:])}")
        i = 1
        for tests in sys.argv[1:]:
            print(f"Argument {i} : {tests}")
            i += 1
    print(f"Argument received : {len(sys.argv)}")


if __name__ == "__main__":
    main()
