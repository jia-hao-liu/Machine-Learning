from numpy import *

T = []
l = 1
Y = []

n = input('How many datas do you input?')
for i in range(int(n)):
  x1 = int(input('x1:'))
  x2 = int(input('x2:'))
  y = int(input('y:'))
  Y.append(y)
  T.append(array([x1,x2]))
w = array([0, 0])
b = 0
flag = 1

arr = 0
while (flag <= 1):
    for arr in range(len(T)):
        if Y[arr] * (w.T.dot(T[arr]) + b) <= 0:
            w = w + l*Y[arr]*T[arr]
            b = b + l*Y[arr]

            flag = 0
            break

    flag += 1

print(w[0], w[1], b)
