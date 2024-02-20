# Step 4: Perform SubBytes operation 
def sub_bytes(state_matrix, s_box):
    """
    Perform the SubBytes operation on the state matrix using the given S-box.
    """
    print(state_matrix)
    for i in range(4):
        for j in range(4):
            byte = state_matrix[i][j]
            state_matrix[i][j] = s_box[int(str(state_matrix[i][j]), 16)]

    return state_matrix