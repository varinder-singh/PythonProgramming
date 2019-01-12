ipAddress = input("Please enter the IP address : ")

segment = ""
length = 0
segment_counter = 1
x = ""
for x in ipAddress:
    if x != '.':
        segment += x
        length +=1
    else:
        print("Segement is {0}  and length of the segment is {1} with total segment count is {2}".format(segment,length,segment_counter))
        segment_counter += 1
        segment = ""
        length = 0
if x != '.':
    print("Segement is {0}  and length of the segment is {1} with total segment count is {2}".format(segment,length,segment_counter))