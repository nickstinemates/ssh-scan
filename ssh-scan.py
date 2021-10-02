#!/usr/bin/env python

PORT = 22

for i in range(0, 256):
    print("nc -vz 10.0.0.%s %s &" % (i, PORT))
