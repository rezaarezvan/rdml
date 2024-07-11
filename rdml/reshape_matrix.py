def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    flat = [item for sublist in a for item in sublist]

    rows, cols = new_shape

    if len(flat) != rows * cols:
        return []

    ans = []
    for i in range(rows):
        row = flat[i*cols: (i+1)*cols]
        ans.append(row)

    return ans
