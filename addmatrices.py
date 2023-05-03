# Define the two matrices to be added
x=[[1,2,3],[2,3,4],[4,5,3]]
y=[[3,4,5],[3,4,3],[3,4,3]]

# Define a new matrix to store the result
result = [[1,1,1], [1, 1, 1], [1, 1, 1]]

# Iterate over each element in the matrices and add them together
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] - y[i][j]

# Print the result
print("The sum of the two matrices is:")
for row in result:
    print(row)

