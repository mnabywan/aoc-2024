def get_lists(filpath):
    list1, list2 = [], []
    with open(filpath) as file:
        lines = [line.rstrip() for line in file]

        for l in lines:
            l_splitted = l.split("   ")
            print(l_splitted)
            list1 += [int(l_splitted[0])]
            list2 += [int(l_splitted[1])]

    return list1, list2

def get_total_distance(list1, list2):
    dist = 0
    for elem1, elem2 in zip(list1, list2):
        dist += abs(elem1 - elem2)
    return dist

def solve_ex1(filepath):
    list1, list2 = get_lists(filepath)
    list1 = sorted(list1)
    list2 = sorted(list2)

    print(list1, list2)

    return get_total_distance(list1, list2)

def get_similarity_score(list1, list2):
    sim_score = 0
    for elem1 in list1:
        sim_score += elem1 * list2.count(elem1) 
    return sim_score

def solve_ex2(filepath):
    list1, list2 = get_lists(filepath)

    return get_similarity_score(list1, list2)
