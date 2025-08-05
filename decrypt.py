import math
import sys

def decrypt(ciphertext: str, key: str) -> str:
    columns = len(key)
    rows = math.ceil(len(ciphertext) / len(key))
    fullcolumns = len(ciphertext) % columns
    if fullcolumns == 0:
        fullcolumns = columns
    
    orderedkey = sorted([(c, i) for i, c in enumerate(key)])
    orderedindices = [i for _, i in orderedkey]

    columnlengths = []
    for pos in range(columns):
        if pos < fullcolumns:
            columnlengths.append(rows)
        else:
            columnlengths.append(rows - 1)

    grid = [""] * columns
    i = 0
    for position, columnindex in enumerate(orderedindices):
        length = columnlengths[position]
        grid[columnindex] = ciphertext[i:i + length]
        i += length
    
    plaintext = ""
    for row in range(rows):
        for column in range(columns):
            if row < len(grid[column]):
                plaintext += grid[column][row]
    return plaintext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Pass arguments in the format of python xxx.py \"ciphertext\" \"key\"")
        sys.exit(1)
    
    text = sys.argv[1]
    key = sys.argv[2]

    decrypted = decrypt(text, key)
    print(decrypted)