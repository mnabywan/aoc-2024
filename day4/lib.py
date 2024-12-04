directions = [
    (0, 1),   # Horizontal (right)
    (1, 0),   # Vertical (down)
    (1, 1),   # Diagonal (down-right)
    (1, -1),  # Diagonal (down-left)
    (0, -1),  # Horizontal (left)
    (-1, 0),  # Vertical (up)
    (-1, -1), # Diagonal (up-left)
    (-1, 1)   # Diagonal (up-right)
]

def get_word_puzzle(filepath):
    with open(filepath) as file:
        lines = file.readlines()
        word_puzzle = [list(line.strip()) for line in lines]
        return word_puzzle

def check_word(word_puzzle, word, num_rows, num_cols, x, y, dx, dy):
    word_length = len(word)
    for i in range(word_length):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= num_rows or ny >= num_cols or word_puzzle[nx][ny] != word[i]:
            return False
    return True


def get_number_of_words(word_puzzle, word):
    num_cols = len(word_puzzle[0])
    num_rows = len(word_puzzle)    
    count = 0

    for r in range(num_rows):
        for c in range(num_cols):
            for dx, dy in directions:
                if check_word(word_puzzle, word, num_rows, num_cols, r, c, dx, dy):
                    count += 1
    return count

def get_number_of_xmas(word_puzzle):
    num_cols = len(word_puzzle[0])
    num_rows = len(word_puzzle)    
    count = 0
    for x in range(1, num_rows-1):
        for y in range(1, num_cols - 1):
            if word_puzzle[x][y] == "A" \
            and {word_puzzle[x - 1][y - 1], word_puzzle[x + 1][y + 1]} == {"M", "S"} \
            and {word_puzzle[x + 1][y - 1], word_puzzle[x - 1][y + 1]} == {"M", "S"}:
                count += 1
    return count

def solve_ex1(filepath, word="XMAS"):
    word_puzzle = get_word_puzzle(filepath)
    return get_number_of_words(word_puzzle, word)

def solve_ex2(filepath):
    word_puzzle = get_word_puzzle(filepath)
    return get_number_of_xmas(word_puzzle)
