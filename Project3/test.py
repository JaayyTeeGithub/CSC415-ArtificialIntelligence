import numpy as np

def sumofsquareddifferences(matrix1, matrix2):
    """Computing the sum of squared differences (SSD) between two images."""
    if len(matrix1) != len(matrix2):
        print("Can't.")
        return
    return np.sum((np.array(matrix1, dtype=np.float32) - np.array(matrix2, dtype=np.float32))**2)


x = [101, 102, 103, 104, 105, 206, 107, 208, 209]
y = [103, 101, 104, 106, 103, 209, 103, 208, 212]
z = [201, 202, 203, 204, 205, 306, 207, 308, 309]

print("d1 and d2:")
print(sumofsquareddifferences(x, y))
print("d1 and d3")
print(sumofsquareddifferences(x, z))
print("d2 and d3")
print(sumofsquareddifferences(y, z))
