def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    '''
    Transpose of a Matrix (easy)

    Write a Python function that computes the transpose of a given matrix.
    Example

    Example:
            input: a = [[1,2,3],[4,5,6]]
            output: [[1,4],[2,5],[3,6]]
            reasoning: The transpose of a matrix is obtained by flipping rows and columns.
    '''

    '''
    Answer:
        The transpose of a matrix a function defined as:
            A := R^{n, m}
            A.T := R^{m, n}

        In simple terms, rotate that thang, rows becomes columns and columns become rows
    '''

    b = []

    for i in range(len(a[0])):
        b.append([row[i] for row in a])

    return b
