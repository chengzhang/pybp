from protobuf.test_pb2 import Foo, Bar
from google.protobuf import json_format

bar = Bar()
bar.z = 'hello'
bar.foo.x = 3
bar.foo.y = 7

dic = json_format.MessageToDict(bar)
print(type(dic))
print(dic)

json_res = json_format.MessageToJson(bar, indent=-1)
print(type(json_res))
print(json_res)
