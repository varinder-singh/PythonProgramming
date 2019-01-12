# writing into a binary file
# using a bytes()

# with open('binary1', 'bw') as binWrite:
#     binWrite.write(bytes(range(10)))
#
# # read the content of the file
# with open('binary1','br') as binRead:
#     for b in binRead:
#         print(b)

a = 65534   # FF FE
b = 65355   # FF FF
c = 65356   # 00 01 00 00
x = 2998302 # 02 2D C0 1E

with open('binary2', 'bw') as binWrite:
    binWrite.write(a.to_bytes(2, 'big'))
    binWrite.write(b.to_bytes(2, 'big'))
    binWrite.write(c.to_bytes(4, 'big'))
    binWrite.write(x.to_bytes(4, 'big'))
    binWrite.write(x.to_bytes(4, 'little'))

with open('binary2', 'br') as binRead:
    e = int.from_bytes(binRead.read(2), 'big')
    print(e)
    f = int.from_bytes(binRead.read(2), 'big')
    print(f)
    g = int.from_bytes(binRead.read(4), 'big')
    print(g)
    h = int.from_bytes(binRead.read(4), 'big')
    print(h)
    i = int.from_bytes(binRead.read(4), 'big') # Number is read in the reverse order as it was saved in the computer memory
    print(i)
