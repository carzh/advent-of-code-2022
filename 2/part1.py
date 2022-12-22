import sys

# CONSTANTS
# there's probably a better way to do this but this is how i'm doing it :)
letter_to_score = {'X': 1,
                   'Y': 2,
                   'Z': 3
                   }
game_to_score = {('A', 'X'): 3, # rock vs rock
                 ('A', 'Y'): 6, # rock vs paper
                 ('A', 'Z'): 0, # rock vs scissor
                 ('B', 'X'): 0, # paper vs rock
                 ('B', 'Y'): 3, # paper vs paper
                 ('B', 'Z'): 6, # paper vs scissor
                 ('C', 'X'): 6, # scissor vs rock
                 ('C', 'Y'): 0, # scissor vs paper
                 ('C', 'Z'): 3, # scissor vs scissor
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
        score += letter_to_score[game[1]] + game_to_score[game]

    return score

if __name__=='__main__':
    main()
