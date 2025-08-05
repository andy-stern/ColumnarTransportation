import math
import sys

def encrypt(plaintext: str, key: str) -> str:
    columns = len(key)
    rows = math.ceil(len(plaintext) / len(key))
    grid = [["" for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            position = i * columns + j
            if position > len(plaintext) - 1:
                break
            grid[i][j] = plaintext[position]

    orderedkey = sorted([(c, i) for i, c in enumerate(key)])
    orderedindices = [i for _, i in orderedkey]

    ciphertext = ""
    for column in orderedindices:
        for row in range(rows):
            if grid[row][column]:
                ciphertext += grid[row][column]
    return ciphertext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Pass arguments in the format of python xxx.py \"plaintext\" \"key\"")
        sys.exit(1)
    
    text = sys.argv[1]
    key = sys.argv[2]

    encrypted = encrypt(text, key)
    print(encrypted)