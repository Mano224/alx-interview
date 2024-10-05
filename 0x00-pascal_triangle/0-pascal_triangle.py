# def permute(string, pocket=""):
#     if len(string) == 0:
#         print(pocket)
#     else:
#         for i in range(len(string)):
#             letter = string[i]
#             front = string[0:i]
#             back = string[i+1:]
#             together = front + back
#             permute(together, letter + pocket)

# print(permute("AB", ""))

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the first row of Pascal's Triangle
    triangle = [[1]]

    for i in range(1, n):
        # Start with 1 for the new row
        row = [1]

        # Compute the values in the middle of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End with 1 for the new row
        row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle

t = pascal_triangle(5)
for row in t:
    print(row)
