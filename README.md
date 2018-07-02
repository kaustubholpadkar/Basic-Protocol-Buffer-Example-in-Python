# Basic-Protocol-Buffer-Example-in-Python
Simple application using Protocol Buffer in Python

## Steps 1 : Create 'point.proto' file 
> syntax = "proto2";
> 
> package point_protocol;
> 
> message Point {
>  optional string label = 1;
>  required float x = 2;
>  required float y = 3;
>}
