from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_block(block, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(block)

def decrypt_block(block, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(block)

def pad(data: bytes) -> bytes:
    blocksize = 16
    padding = blocksize - (len(data) % blocksize)
    lil = bytes([padding] * padding)
    return data + lil

def unpad(data: bytes) -> bytes:
    blocksize = 16
    pad_len = data[-1]

    if pad_len < 1 or pad_len > blocksize:
        raise ValueError("padding wrong")

    return data[:-pad_len]

def ECB(data: bytes, key):
    data = pad(data)
    res = bytearray()

    for i in range(0, len(data), 16):
        block = data[i:i + 16]
        res += encrypt_block(block, key)

    return bytes(res)

def CBC(data: bytes, key, iv):
    data = pad(data)
    res = bytearray()
    prev = iv

    for i in range(0, len(data), 16):
        block = data[i:i + 16]

        xored = bytes(a ^ b for a, b in zip(block, prev))
        encrypted = encrypt_block(xored, key)

        res += encrypted
        prev = encrypted

    return bytes(res)

if __name__ == '__main__':
    key = b"epic sauses12345"   # 16 bytes
    iv = get_random_bytes(16)

    with open("cp-logo.bmp", "rb") as file:
        binary_data = file.read()
        header = binary_data[:54]
        data = binary_data[54:]

    encrypted_data1 = ECB(data, key)
    encrypted_data2 =CBC(data,key,iv)

    with open("output2.bmp", "wb") as f:
        f.write(header + encrypted_data2)

    with open("output1.bmp", "wb") as f:
        f.write(header + encrypted_data1)

    print(encrypted_data2)
# :) Implement PKCS#7 padding and unpadding.
# :)Implement AES-ECB block encryption/decryption using the library primitive.
# Build your own ECB mode on top of that.
# Build your own CBC mode on top of that.
# Encrypt a BMP image with ECB and CBC, preserving the header.
# Write submit() and verify().
# Perform the CBC bit-flipping attack.
# Run openssl speed RSA and openssl speed AES.
# Make the two graphs.
# Write the report and export it to PDF.