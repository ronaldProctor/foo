#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this will add "dns" to the end of our list
protoa.append("dns") # this will add "dna" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument of the extend method
print(protoa)

protoa.insert(0,"foo") # insert "foo" into the first spot on the list
print(protoa)
