def sort_matrix_by_row(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            min_index = j
            for k in range(j+1, len(matrix[i])):
                if matrix[i][k] < matrix[i][min_index]:
                    min_index = k
            if min_index != j:
                matrix[i][j], matrix[i][min_index] = matrix[i][min_index], matrix[i][j]
    return matrix

def sort_rectangles(title):
    rectangles = [ 
        {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, 
        {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
    ]
    n = len(rectangles)
    for i in range(1, n):
        j = i
        while j > 0 and rectangles[j][title] < rectangles[j-1][title]:
            rectangles[j], rectangles[j-1] = rectangles[j-1], rectangles[j]
            j -= 1
    return rectangles


matrix = [[5,8,1],[6,7,3],[5,4,9]]
sorted_matrix = sort_matrix_by_row(matrix)
print(sorted_matrix)

matrix1 = [['banana', 'apple', 'pear'],
          ['dog', 'cat', 'bird'],
          ['chocolate', 'vanilla', 'strawberry']]
sorted_matrix1 = sort_matrix_by_row(matrix1)
print(sorted_matrix1)

print(sort_rectangles("ID"))
print(sort_rectangles("Length"))
print(sort_rectangles("Breadth"))
print(sort_rectangles("Color"))



