import lib

filepath = "input/input2"

if __name__ == "__main__":
    safe_reports = lib.solve_ex2(filepath)
    print(f"Number of safe reports with removal: {safe_reports}")
