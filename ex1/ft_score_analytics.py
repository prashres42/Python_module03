import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    scores = []
    for n in sys.argv[1:]:
        try:
            score = int(n)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{n}'")
    Total_player = len(scores)
    if scores:
        print(f"Scores processed : {scores}")
        print(f"Total player: {Total_player}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    if not scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
