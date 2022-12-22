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
    group_rucksacks = parse_file(path)
    print(calculate_score(group_rucksacks))

def print_usage():
    print("please pass in the input file path as the first argument")
        
def parse_file(file_path):
    """
    Returns a list of list of strings
    """
    f = open(file_path)
    lines = f.read().splitlines()

    list_2d = []
    list_1d = []

    for line in lines:
        list_1d.append(line)
        if len(list_1d) == 3:
            list_2d.append(list_1d)
            list_1d = []

    if len(list_1d) > 0:
        list_2d.append(list_1d)
            
    return list_2d

# ---------------------------------------------------------------------------------------

def calculate_score(group_rucksacks):
    priorities = create_priority_map()
    score = 0

    for group_rucksack in group_rucksacks:
        duplicate = find_shared(group_rucksack)

        if duplicate is None:
            print('something went wrong -- couldn\'t find duplicate in this string:')
            print(rucksack)
            exit()
        score += priorities[duplicate]

    return score

def find_shared(rucksacks):
    # this method is so ugly :(
    seen = set()
    for item in rucksacks[0]:
        seen.add(item)

    shared_2 = set()
    for item in rucksacks[1]:
        if item in seen:
            shared_2.add(item)

    for item in rucksacks[2]:
        if item in shared_2:
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
