import typing
import random

actions = list(["run", "eat", "sleep", "move", "grab", "climb",
                "release"])
players = list(["Alice", "Bob", "Charlie", "Dylan"])


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(trash: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while trash:
        take_one = random.choice(trash)
        trash.remove(take_one)
        yield take_one


if __name__ == "__main__":
    iterator = gen_event()
    for n in range(10):
        name, action = next(iterator)
        print(f"Event {n}: Player {name} did action {action}")
    pl_detail = []
    for n in range(10):
        pl_detail.append(next(iterator))
    n = len(pl_detail)
    print(f"Built list of {n} events: {pl_detail}")
    for event in consume_event(pl_detail):
        print(f"Got event from list: {event}")
        print(f"Remained in the list: {pl_detail}")
