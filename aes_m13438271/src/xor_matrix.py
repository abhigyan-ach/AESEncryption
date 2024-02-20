def xor_with_original(state_matrix, subkey_matrix):
    """
    Perform an XOR operation between corresponding elements of two matrices.
    """
    result_matrix = []
    for i in range(4):  # Iterate over rows
        row = []
        for j in range(4):  # Iterate over columns
            xor_result = int(str(state_matrix[i][j]),16) ^ int(str(subkey_matrix[i][j]),16)  # Perform XOR operation
            row.append(xor_result)
        result_matrix.append(row)
    return result_matrix