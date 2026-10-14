import sys
class Score_error(Exception):
    def __init__(self, messaage: str):
        self.message = message
    
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = []
    Total_player = len(sys.argv[1:])
    try:
        for n in sys.argv[1:]:
            try:
                score = int(n)
                scores.append(score)
            except ValueError:
                continue
        if scores:
            print(f"Scores processed : {scores}")
            print(f"Total player: {Total_player}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores)/2}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
    except:
