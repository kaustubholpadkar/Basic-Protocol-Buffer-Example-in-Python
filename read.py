import point_pb2

point = point_pb2.Point()

f = open("storage_file.txt", "rb")
point.ParseFromString(f.read())
f.close()

print(point.label)
print(point.x)
print(point.y)
