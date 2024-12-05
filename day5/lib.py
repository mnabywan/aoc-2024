
def parse_input(filepath):
    data = []
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]

    rules = {}
    update_data = []

    for line in lines:
        if "|" in line:
            prev, after = line.split("|")
            prev, after = int(prev), int(after)
            if prev not in list(rules.keys()):
                rules[prev] = [after]
            else:
                rules[prev].append(after)
            if after not in list(rules.keys()):
                rules[after] = []

        else:
            if "," in line:
                update_data.append([int(el) for el in line.split(",")])

    return rules, update_data

def is_data_correct(rules, update_data, data):
    keys_ = list(rules.keys())
    for i, el in enumerate(data):
        prev = data[0:i]
        after = data[i+1:-1]
        for p in prev:
            if p in rules[el]:
                return False
        for a in after:
            if el in rules[a]:
                return False
    return True

def sum_enabled_multiplication_results(rules, update_data):
    sum_ = 0
    for data in update_data:
        if is_data_correct(rules, update_data, data):
            sum_ += data[len(data)//2]
    return sum_

def sort_pages(update, rule_dict):
    n = len(update)
    sorted_update = update[:]
  
    # Keep sorting until no changes are made
    for _ in range(n):
        swapped = False
        for i in range(n - 1):
            a = sorted_update[i]
            b = sorted_update[i + 1]
      
            if a in rule_dict and b in rule_dict[a]:
                sorted_update[i], sorted_update[i + 1] = sorted_update[i + 1], sorted_update[i]
                swapped = True

        if not swapped:
            break

    return sorted_update

def is_ordered(update, rule_dict):
    page_index = {page: i for i, page in enumerate(update)}
    for a, dependencies in rule_dict.items():
        if a not in page_index: # page not in update, so we don't check it
            continue
        for b in dependencies:
            if b in page_index and page_index[a] > page_index[b]:
                return False  # rule was not followed
      
    return True

def sum_fixed_results(rules, update_data):
    middle_pages = []

    for update in update_data:
        if not is_ordered(update, rules):
            ordered_update = sort_pages(update, rules)
            middle_index = len(ordered_update) // 2 
            middle_pages.append(ordered_update[middle_index])

    return sum(middle_pages)

def solve_ex1(filepath):
    rules, update_data = parse_input(filepath)
    return sum_enabled_multiplication_results(rules, update_data)

def solve_ex2(filepath):
    rules, update_data = parse_input(filepath)
    return sum_fixed_results(rules, update_data)
