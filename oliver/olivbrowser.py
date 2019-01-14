import struct

print('Welcome to the olivbrowsr')


f = open('example.OLV', 'rb')
header = f.read(4)
length = f.read(4)

decoded_length = struct.unpack('>i', length)[0]


print(decoded_length)



f.close()
