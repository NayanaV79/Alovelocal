def pascals_triangle(num_rows):
    if num_rows <= 0:
        return []

    triangle = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
num_rows = int(input("numRows="))
result_triangle = pascals_triangle(num_rows)
print(result_triangle)
#algorithm
'''
first step is to define a function with a parameter which take input of rows
Next is to check if num_rows is less than or equal to 0.If its true, return an empty list.
if not Create a list triangle and initialize it with a list containing the first row [1].
to generate rows Use a loop starting from 1 up to num_rows - 1 to generate each row.
Initialize an empty list row for the current row with the first element as 1.
Use another loop starting from 1 up to i - 1 to calculate each element in the row.
Append the sum of the corresponding elements from the previous row to the row list.
Append 1 to the end of the row list.
Append the generated row to the triangle list
'''
