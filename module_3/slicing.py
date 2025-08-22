

import numpy as np


f = "/Users/anthonyrubio/Downloads/data/m10x10_int.txt";

m10x10 = np.loadtxt(f)

print(m10x10[:2])
print("====")
print(m10x10[:8,:])
print("====")
print(m10x10[:8,2:])
print("====")
print(m10x10[2:,2:])
print("====")
print(m10x10[2:8,2:])

m333 = np.random.randint(0, 10,(3,3,3))
print("====")
print(m333)
print("====")
print(m333[:,:,:])
print("====")
print(m333[1,:,:])
print("====")
print(m333[1,1,:])
print("====")
print(m333[1,1,1])

#fancy slicing

print("====")
print(m333[[0,2],:,:])
print("====")
print(m333[:,[0,2],:])
print("====")
print(m333[:,:,[0,2]])

