def plaintext_to_state_matrix(plaintext):
    """
    Convert plaintext to a state matrix represented in hexadecimal form.
    """
    state_matrix = []
    for i in range(4):  # Iterate over columns
        column = []
        for j in range(i, len(plaintext), 4):  # Iterate over each character in the column
            ascii_value = ord(plaintext[j])
            hex_value = format(ascii_value, '02x')
            column.append(hex_value)
        # If there are fewer than 4 bytes in the column, pad with '00'
        while len(column) < 4:
            column.append('00')
        state_matrix.append(column)
    return state_matrix