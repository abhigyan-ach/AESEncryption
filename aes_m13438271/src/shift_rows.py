def shift_rows(matrix):
    """
    Shift rows of the matrix according to AES encryption standard.
    """
    shifted_matrix = []
    for i, row in enumerate(matrix):
        shifted_row = row[i:] + row[:i]  # Perform cyclic left shift for each row
        shifted_matrix.append(shifted_row)
    return shifted_matrix