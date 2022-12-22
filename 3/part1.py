import sys

# CONSTANTS
# ---------------------------------------------------------------------------------------

def main():
    path = ""
    try:
        path = sys.argv[1]
    except:
        print_usage()
        exit()
    rucksacks = parse_file(path)
    print(calculate_score(rucksacks))

def print_usage():
    print("please pass in the input file path as the first argument")
        
def parse_file(file_path):
    """
    Returns a list of strings
    """
    f = open(file_path)
    lines = f.read().splitlines()

    list_1d = []

    for line in lines:
        list_1d.append(line)
            
    return list_1d

# ---------------------------------------------------------------------------------------

def calculate_score(rucksacks):
    priorities = create_priority_map()
    score = 0

    for rucksack in rucksacks:
        halfway = int(len(rucksack) / 2)
        first_half = rucksack[:halfway]
        second_half = rucksack[halfway:]
        duplicate = find_shared(first_half, second_half)

        if duplicate is None:
            print('something went wrong -- couldn\'t find duplicate in this string:')
            print(rucksack)
            exit()
        score += priorities[duplicate]

    return score

def find_shared(comp1, comp2):
    seen = set()
    for item in comp1:
        seen.add(item)

    for item in comp2:
        if item in seen:
            return item
    return None

def create_priority_map():
    priorities = {}
    # lowercase priorities
    for i in range(1, 27):
        priorities[chr(96 + i)] = i

    # uppercase priorities
    for i in range(1, 27):
        priorities[chr(64 + i)] = 26 + i
    return priorities

if __name__=='__main__':
    main()
