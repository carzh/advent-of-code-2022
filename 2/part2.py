import sys

# CONSTANTS
# there's probably a better way to do this but this is how i'm doing it :)
letter_to_score = {'rock': 1,
                   'paper': 2,
                   'scissor': 3
                   }
result_to_score = {'X': 0,
                   'Y': 3,
                   'Z': 6
                   }
# X = you need to lose
# Y = you need to draw
# Z = you need to win
game_to_score = {('A', 'X'): 'scissor', # rock vs scissor
                 ('A', 'Y'): 'rock', # rock vs rock
                 ('A', 'Z'): 'paper', # rock vs paper
                 ('B', 'X'): 'rock', # paper vs rock
                 ('B', 'Y'): 'paper', # paper vs paper
                 ('B', 'Z'): 'scissor', # paper vs scissor
                 ('C', 'X'): 'paper', # scissor vs paper
                 ('C', 'Y'): 'scissor', # scissor vs scissor
                 ('C', 'Z'): 'rock', # scissor vs rock
                 }
# ---------------------------------------------------------------------------------------

def main():
    path = ""
    try:
        path = sys.argv[1]
    except:
        print_usage()
        exit()
    games = parse_file(path)
    print(calculate_score(games))

def print_usage():
    print("please pass in the input file as the first argument")
        
def parse_file(file_path):
    """
    Returns a list of tuples
    """
    f = open(file_path)
    lines = f.read().splitlines()

    list_1d = []

    for line in lines:
        list_1d.append(tuple(line.split()))
            
    return list_1d

# ---------------------------------------------------------------------------------------

def calculate_score(games):
    score = 0
    for game in games:
        score += letter_to_score[game_to_score[game]] + result_to_score[game[1]]

    return score

if __name__=='__main__':
    main()
