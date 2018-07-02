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
protoc -I=$SRC_DIR --python_out=. point.proto
```
