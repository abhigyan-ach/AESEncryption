def hex_to_matrix(hex_key):
    # Split the hexadecimal string into chunks of 2 characters each
    hex_chunks = [hex_key[i:i+2] for i in range(0, len(hex_key), 2)]

    # Convert hexadecimal chunks into integer values
    key_integers = [int(chunk, 16) for chunk in hex_chunks]

    # Reshape the integers into a 4 by 4 matrix
    state_matrix = [
        key_integers[0::4],
        key_integers[1::4],
        key_integers[2::4],
        key_integers[3::4]
    ]

    return state_matrix