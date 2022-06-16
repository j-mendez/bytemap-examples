import struct

# list of bytemaps
bytemap = []

# default bytetable
bytetable = {
    128: 0,
    64: 0,
    32: 0,
    16: 0,
    8: 0,
    4: 0,
    2: 0,
    1: 0,
    0: 0
}

rawFile = open ("font.bin", "rb") #binary data

for x in range (128): # first 128 standard
    for y in range (8): # byte range
        data = rawFile.read(1)
        (value) = struct.unpack ('B', data)
        byte = value[0]
        bitm = bytetable.copy()

        # loop through default map to assign
        for k in bitm:
            bitm[k] = 1 if byte & k else 0
        bytemap.append(bitm)

# iterate through bytemap and collect results
for byte in bytemap:
    result = []
    for i in byte:
        item = byte[i]
        if item == 1:
            result.append("x")
        else:
            result.append(" ")
    print(''.join(result))