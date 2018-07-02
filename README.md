# Basic-Protocol-Buffer-Example-in-Python
Simple application using Protocol Buffer in Python

## Step 1 : Create 'point.proto' 

```python
syntax = "proto2";
 
package point_protocol;
 
message Point {
  optional string label = 1;
  required float x = 2;
  required float y = 3;
}
```

## Step 2 : Compile 'point.proto' and generate 'point_pb2.py'

```terminal
$ protoc -I=$SRC_DIR --python_out=. point.proto
```
## Step 3 : Create 'write.py' to write point object to file

```python
import point_pb2

point = point_pb2.Point()

point.label = "first_point"
point.x = 3
point.y = 4

# write the object point in 'storage_file.txt'
f = open("storage_file.txt", "wb")          # open stream
f.write(point.SerializeToString())          # write to file
f.close()                                   # close stream

```


## Step 4 : Create 'read.py' to read point object from file

```python
import point_pb2

point = point_pb2.Point()

f = open("storage_file.txt", "rb")
point.ParseFromString(f.read())
f.close()

print(point.label)
print(point.x)
print(point.y)

```
