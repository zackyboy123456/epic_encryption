def pad(data: bytes) -> bytes:
    blocksize = 16
    padding = blocksize - (len(data) % blocksize)
    lil = bytes([padding] * padding)
    return data + lil


def unpad(data: bytes) -> bytes:
    blocksize = 16
    pad = data[-1]

    if pad < 1 or pad > blocksize:
        raise ValueError("padding wrong")
    return data[:-pad]
if __name__ == '__main__':
    s = b"heya sexy fellows"
    lel = pad(s)
    print(pad(s))
    print(unpad(lel))

# :) Implement PKCS#7 padding and unpadding.
# Implement AES-ECB block encryption/decryption using the library primitive.
# Build your own ECB mode on top of that.
# Build your own CBC mode on top of that.
# Encrypt a BMP image with ECB and CBC, preserving the header.
# Write submit() and verify().
# Perform the CBC bit-flipping attack.
# Run openssl speed RSA and openssl speed AES.
# Make the two graphs.
# Write the report and export it to PDF.