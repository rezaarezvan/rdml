def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    '''
    Matrix times Vector (easy)

    Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
    Example

    Example:
            input: a = [[1,2],[2,4]], b = [1,2]
            output:[5, 10]
            reasoning: 1*1 + 2*2 = 5;
                       1*2+ 2*4 = 10
    '''

    '''
    Answer:
        For a matrix-vector multiplication with matrix `A` and vector `b`, we need that:

        A := m x _n_
        b := _n_ x 1

        Then the dot product is defined as:

        Ab = [[a_11 * b_1 + a_12 * b_2 + ... + a_1n * b_n], [a_21 * x_1 + ... a_2n * x_n], ...]

    '''

    if len(a[0]) != len(b):
        return -1

    c = []

    for row in a:
        sum = 0
        for x, y in zip(row, b):
            sum += x*y
        c.append(sum)

    return c
