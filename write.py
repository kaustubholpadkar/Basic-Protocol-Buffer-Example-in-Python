import point_pb2

point = point_pb2.Point()

point.label = "first_point"
point.x = 3
point.y = 4

# write the object point in 'storage_file.txt'
f = open("storage_file.txt", "wb")          # open stream
f.write(point.SerializeToString())          # write to file
f.close()                                   # close stream
