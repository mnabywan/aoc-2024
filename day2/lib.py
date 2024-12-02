def is_strictly_increasing_or_decreasing(arr):
    return all(i < j for i, j in zip(arr, arr[1:])) or all(i > j for i, j in zip(arr, arr[1:]))

def get_differences(arr):
    return [arr[i]-arr[i-1] for i in range(1, len(arr))]

def get_report_data(filepath):
    data = [] 
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]
    
    for line in lines:
        l_parsed = [int(el) for el in line.split(" ")]
        data.append(l_parsed)

    return data

def count_safe_reports(data):
    num_safe_reports = 0
    for d in data:
        diff = get_differences(d)
        if all(el > 0 and el <= 3 for el in diff) or all(el < 0 and el >= -3 for el in diff):
            num_safe_reports += 1
    return num_safe_reports


def remove_element_by_index(array, index):
    if index < 0 or index >= len(array):
        raise IndexError("Index out of range")
    # Remove the element by slicing
    return array[:index] + array[index+1:]

def is_safe_with_removal(array):
    diff = get_differences(array)
    if all(el > 0 and el <= 3 for el in diff) or all(el < 0 and el >= -3 for el in diff):
        return True

    for i, _ in enumerate(array):
        arr_removed = remove_element_by_index(array, i)
        new_diff = get_differences(arr_removed)
        if all(el > 0 and el <= 3 for el in new_diff) or all(el < 0 and el >= -3 for el in new_diff):
            return True
    return False

def count_safe_reports_with_removal(data):
    num_safe_reports = 0
    for d in data:
        if is_safe_with_removal(d):
            num_safe_reports += 1
    return num_safe_reports

def solve_ex1(filepath):
    data = get_report_data(filepath)
    return count_safe_reports(data)

def solve_ex2(filepath):
    data = get_report_data(filepath)
    return count_safe_reports_with_removal(data)
