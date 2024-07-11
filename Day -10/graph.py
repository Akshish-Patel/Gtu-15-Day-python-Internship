import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# matplotlib library is use the create a simple, low level graph

# gives the version of the matplotlib library
print(matplotlib.__version__)

# line plot or graph
xpoint = np.array([0,6])
ypoint = np.array([0,250])
print("xpoint = ",xpoint)
print("ypoint = ",ypoint)

# plt.plot method is use to make a line graph
plt.plot(xpoint, ypoint)
plt.show()

# plot the graph without line
x_point = np.array([3, 9])
y_point = np.array([3, 9])

plt.plot(x_point, y_point, 'o') # this method is use to make only two dot whic is (3,3) and (9,9)
plt.show()


# multiple line plot
x_point = np.array([1,3,5,7,9])
y_point = np.array([10,6,2,4,8])

plt.plot(x_point, y_point) 
plt.show()
