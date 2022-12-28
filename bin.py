import numpy as np
a = np.array([])
s = np.array([])
s1 = np.array([])
s = np.append(s, [1 ,2])
s1 = np.append(s1, [3, 4])
a = np.append(a, s)
a = np.append(a, s1)
a = a.reshape(2,2)
print(a[0][1])
str = b"Hello"
str1 = "Hello п"
print(str1.encode("utf-8"))
