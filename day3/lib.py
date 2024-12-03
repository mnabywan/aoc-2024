import re

def get_data(filepath, pattern):
    data = []
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]
    
    for line in lines:
        matches = re.findall(pattern, line)
        for m in matches:
            data.append(m)
    print(data)
    return data

def sum_multiplication_results(data, pattern):
    result = 0

    for d in data:
        match = re.search(pattern, d)
        if match:
            result += int(match.group(1)) * int(match.group(2))
    return result

def sum_enabled_multiplication_results(data, pattern):
    result = 0
    multiplication_enabled = True

    for d in data:
        if d == "don't()":
            multiplication_enabled = False
            continue
        elif d == "do()":
            multiplication_enabled = True
            continue
        
        match = re.search(pattern, d)
        if match:
            print(match.group(0))
  
            if multiplication_enabled:
                result += int(match.group(1)) * int(match.group(2))
    return result

def solve_ex1(filepath):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    search = r"mul\((\d+),(\d+)\)"
    data = get_data(filepath, pattern)
    return sum_multiplication_results(data, search)

def solve_ex2(filepath):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"    
    search = r"mul\((\d+),(\d+)\)"
    data = get_data(filepath, pattern)
    return sum_enabled_multiplication_results(data, search)
