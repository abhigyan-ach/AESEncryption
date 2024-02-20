import plaintext_convert
import hex_to_matrix
import xor_matrix
import sub_bytes
import shift_rows
import mix_columns
import numpy as np

def main():
    # Your main code goes here
    #SubBytes Operation
    s_box = (
        0x63,
        0x7C,
        0x77,
        0x7B,
        0xF2,
        0x6B,
        0x6F,
        0xC5,
        0x30,
        0x01,
        0x67,
        0x2B,
        0xFE,
        0xD7,
        0xAB,
        0x76,
        0xCA,
        0x82,
        0xC9,
        0x7D,
        0xFA,
        0x59,
        0x47,
        0xF0,
        0xAD,
        0xD4,
        0xA2,
        0xAF,
        0x9C,
        0xA4,
        0x72,
        0xC0,
        0xB7,
        0xFD,
        0x93,
        0x26,
        0x36,
        0x3F,
        0xF7,
        0xCC,
        0x34,
        0xA5,
        0xE5,
        0xF1,
        0x71,
        0xD8,
        0x31,
        0x15,
        0x04,
        0xC7,
        0x23,
        0xC3,
        0x18,
        0x96,
        0x05,
        0x9A,
        0x07,
        0x12,
        0x80,
        0xE2,
        0xEB,
        0x27,
        0xB2,
        0x75,
        0x09,
        0x83,
        0x2C,
        0x1A,
        0x1B,
        0x6E,
        0x5A,
        0xA0,
        0x52,
        0x3B,
        0xD6,
        0xB3,
        0x29,
        0xE3,
        0x2F,
        0x84,
        0x53,
        0xD1,
        0x00,
        0xED,
        0x20,
        0xFC,
        0xB1,
        0x5B,
        0x6A,
        0xCB,
        0xBE,
        0x39,
        0x4A,
        0x4C,
        0x58,
        0xCF,
        0xD0,
        0xEF,
        0xAA,
        0xFB,
        0x43,
        0x4D,
        0x33,
        0x85,
        0x45,
        0xF9,
        0x02,
        0x7F,
        0x50,
        0x3C,
        0x9F,
        0xA8,
        0x51,
        0xA3,
        0x40,
        0x8F,
        0x92,
        0x9D,
        0x38,
        0xF5,
        0xBC,
        0xB6,
        0xDA,
        0x21,
        0x10,
        0xFF,
        0xF3,
        0xD2,
        0xCD,
        0x0C,
        0x13,
        0xEC,
        0x5F,
        0x97,
        0x44,
        0x17,
        0xC4,
        0xA7,
        0x7E,
        0x3D,
        0x64,
        0x5D,
        0x19,
        0x73,
        0x60,
        0x81,
        0x4F,
        0xDC,
        0x22,
        0x2A,
        0x90,
        0x88,
        0x46,
        0xEE,
        0xB8,
        0x14,
        0xDE,
        0x5E,
        0x0B,
        0xDB,
        0xE0,
        0x32,
        0x3A,
        0x0A,
        0x49,
        0x06,
        0x24,
        0x5C,
        0xC2,
        0xD3,
        0xAC,
        0x62,
        0x91,
        0x95,
        0xE4,
        0x79,
        0xE7,
        0xC8,
        0x37,
        0x6D,
        0x8D,
        0xD5,
        0x4E,
        0xA9,
        0x6C,
        0x56,
        0xF4,
        0xEA,
        0x65,
        0x7A,
        0xAE,
        0x08,
        0xBA,
        0x78,
        0x25,
        0x2E,
        0x1C,
        0xA6,
        0xB4,
        0xC6,
        0xE8,
        0xDD,
        0x74,
        0x1F,
        0x4B,
        0xBD,
        0x8B,
        0x8A,
        0x70,
        0x3E,
        0xB5,
        0x66,
        0x48,
        0x03,
        0xF6,
        0x0E,
        0x61,
        0x35,
        0x57,
        0xB9,
        0x86,
        0xC1,
        0x1D,
        0x9E,
        0xE1,
        0xF8,
        0x98,
        0x11,
        0x69,
        0xD9,
        0x8E,
        0x94,
        0x9B,
        0x1E,
        0x87,
        0xE9,
        0xCE,
        0x55,
        0x28,
        0xDF,
        0x8C,
        0xA1,
        0x89,
        0x0D,
        0xBF,
        0xE6,
        0x42,
        0x68,
        0x41,
        0x99,
        0x2D,
        0x0F,
        0xB0,
        0x54,
        0xBB,
        0x16,
    )
    print("Length of S Box",len(s_box),"\n") 
    with open("/Users/abhiacherjee/Desktop/Spring 2024/CS5153/aes_m13438271/data/plaintext.txt", "r") as file:
        message = file.read()

    state_matrix = plaintext_convert.plaintext_to_state_matrix(message)
    
    # Convert each character into ASCII and pad to ensure 128 bits
    ascii_message = [ord(char) for char in message]
    while len(ascii_message) < 16:
        ascii_message.append(0)

    #Step 2: Read the two subkeys from the file
    with open("/Users/abhiacherjee/Desktop/Spring 2024/CS5153/aes_m13438271/data/subkey_example.txt", "r") as file:
        subkey0 = file.readline().strip()
        subkey1 = file.readline().strip()
    

    # Convert hexadecimal subkey into a 4 by 4 state matrix
    s_matrix = hex_to_matrix.hex_to_matrix(subkey0)
    s_matrix = [['{:02x}'.format(i) for i in row] for row in s_matrix]

    # Display the state matrix
    print("Subkey0 Matrix:\n")
    for row in s_matrix:
        print(row)


    result = xor_matrix.xor_with_original(state_matrix, s_matrix)
    print("Resultant Matrix after AddKey:\n")
    # Display the result
    # for row in result:
    #     print(row)

    state_matrix=result
    state_matrix = [['{:02x}'.format(i) for i in row] for row in state_matrix]


    state_matrix = sub_bytes.sub_bytes(state_matrix, s_box)
    print("Resultant Matrix after SubBytes:\n")
    state_matrix = [['{:02x}'.format(i) for i in row] for row in state_matrix]

    for row in state_matrix:
       print(row)
    
    shifted_state = shift_rows.shift_rows(state_matrix)
    state_matrix=shifted_state
    print("Resultant Matrix after SubBytes:\n")

    for row in state_matrix:
        print(row)
    
    ##MixColumns Operation
    #print("Resultant Matrix after SubBytes:\n")

    resultant_matrix = mix_columns.mix_columns(state_matrix)

    #print("Resultant Matrix:")
    # print(resultant_matrix)
    state_matrix=resultant_matrix
    # print(type(state_matrix[0][0]))
    state_matrix = [['{:02x}'.format(int(i)) for i in row] for row in state_matrix]
    print("Resultant Matrix after MixColumns:\n")

    for row in state_matrix:
        print(row)

    
    #Convert Subkey1 to matrix and perform AddKey Operation
    subkey_hex = subkey1

    # Convert hexadecimal subkey into a 4 by 4 state matrix
    s_matrix2 = hex_to_matrix.hex_to_matrix(subkey_hex)
    s_matrix2 = [['{:02x}'.format(i) for i in row] for row in s_matrix2]
    # Display the state matrix
    print("Subkey1 Matrix \n")
    for row in s_matrix2:
        print(row)
    result = xor_matrix.xor_with_original(state_matrix, s_matrix2)

    # Display the result
    # for row in result:
    #     print(row)    
    #hex_matrix = [[hex(num) for num in row] for row in state_matrix]
    state_matrix = [['{:02x}'.format(i) for i in row] for row in result]

    # Display the hexadecimal matrix
    print("Resultant Matrix after AddKey with SubKey1:\n")

    for row in state_matrix:
        print(row)
   
    with open("/Users/abhiacherjee/Desktop/Spring 2024/CS5153/aes_m13438271/data/result.txt", "w") as file:
        #file.write(state_matrix)
        for row in state_matrix:
            file.write(str(row))
            file.write("\n")
   
if __name__ == "__main__":
    main()