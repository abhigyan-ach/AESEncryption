import numpy as np
    
def mix_columns(state):
    """
    Mix columns of the state matrix using AES MixColumns operation.
    """
    polynomial_matrix = np.array(
        [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]], dtype=np.uint8
    )

    mixed_state = np.zeros((4, 4))

    #print("type:",type(mixed_state[0][0]))
    for i in range(4):
        for j in range(4):
            mixed_state[i][j] = (
                gf_mul(polynomial_matrix[i][0], state[0][j])
                ^ gf_mul(polynomial_matrix[i][1], state[1][j])
                ^ gf_mul(polynomial_matrix[i][2], state[2][j])
                ^ gf_mul(polynomial_matrix[i][3], state[3][j])
            )
            #print(type(mixed_state[i][j]))

    #return mixed_state.tolist()
    return mixed_state


def gf_mul(a, b): #Source: StackOverflow 
    """
    Galois Field (GF(2^8)) multiplication of two numbers.
    """
    p = 0b100011011             
    m = 0           
    # print("B is:",b)
    # print("\n",type(b))
    # a = int(a,16) #if isinstance(a, str) else a  # Convert 'a' to integer if it's a string
    b = int(b,16) if isinstance(b, str) else b  #     
    # print("B is:",b)
    # print("\n",type(b))       
    for i in range(8):
        m = m << 1
        if m & 0b100000000:
            m = m ^ p
        if b & 0b010000000:
            m = m ^ a
        b = b << 1
    return m

def hex_to_ascii(state_matrix):
    """
    Convert hexadecimal state matrix to ASCII characters.
    """
    ascii_matrix = []
    for row in state_matrix:
        #print(row)
        ascii_row = ''.join([(int(str(hex_value), 16)) for hex_value in row])
        ascii_matrix.append(ascii_row)
    return ascii_matrix