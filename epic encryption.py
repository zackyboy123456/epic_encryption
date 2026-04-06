
def pad(data :bytes) ->bytes :
    blocksize = 16
    padding = blocksize - (len(data) % blocksize)
    lil = bytes([padding] * padding)
    return data + lil

def unpad(data :bytes) -> bytes:
    blocksize =16
    pad =data[-1]
    if pad < 1 or pad > blocksize:
        raise ValueError("padding wrong")

    else:
        return data[:-pad]

if __name__ == '__main__':

