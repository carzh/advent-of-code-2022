PATH_TO_INPUT = 'input.txt'

def main():
    reindeer_cals = file_into_2d_list(PATH_TO_INPUT)
    reindeer_sums = sum_reindeer_cals(reindeer_cals)
    reindeer_sums.sort(reverse=True)
    print(sum(reindeer_sums[:3]))

def file_into_2d_list(file_path):
    list_2d = []

    f = open(file_path)
    lines = f.read().splitlines()

    list_1d = []

    for line in lines:
        if len(line.strip()) > 0:
            list_1d.append(int(line))
        elif len(list_1d) > 0:
            list_2d.append(list_1d)
            list_1d = []

    if len(list_1d) > 0:
        list_2d.append(list_1d)
        list_1d = []
    return list_2d

def sum_reindeer_cals(reindeer_cals):
    return [sum(reindeer_cal_list) for reindeer_cal_list in reindeer_cals]


def find_max(reindeer_cals):
    max_so_far = float('-inf')
    for reindeer in reindeer_cals:
        total_cals = sum(reindeer)
        if total_cals > max_so_far:
            max_so_far = total_cals
    return max_so_far

if __name__=='__main__':
    main()
