import base64

input_string = input("Enter a word for encryption: ")
encryption_key = input("Enter an encryption key: ")


def printable_encrypted_string(string):
    """
    Encrypted message is not readable, because contains a lot of
    non printable symbols like a tabulation, new-line and etc
    So we convert this message to base64 encoded string
    """
    message_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("ascii")


def get_key_symbol(key, index):
    """
    If length of our key is less than initial string
    we get next symbol from the start in a loop
    """
    if index > len(key) - 1:
        return key[index % len(key)]
    return key[index]


def xor_cipher(string, key):
    result = []
    for index, symbol in enumerate(string):
        result.append(chr(ord(symbol) ^ ord(get_key_symbol(key, index))))
    return "".join(result)


encrypted_string = xor_cipher(input_string, encryption_key)
print("Encrypted string: " + printable_encrypted_string(encrypted_string))

decrypted_string = xor_cipher(encrypted_string, encryption_key)
print("Decrypted string: " + decrypted_string)