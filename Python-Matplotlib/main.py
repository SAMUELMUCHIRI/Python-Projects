import matplotlib.pyplot as plt
import numpy as np
def plot1():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])
    #adding the o erases the line only showing two points in a graph

    plt.plot(xpoints, ypoints)
    plt.show()
def plot2():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints, 'o')
    plt.show()
def plot3():
    xpoints = np.array([1, 2, 6, 8])
    ypoints = np.array([3, 8, 1, 10])
    plt.plot(xpoints, ypoints)
    plt.show()
def plot4():
    '''If we do not specify the points on the x-axis, 
    they will get the default values 0, 1, 2, 3 (etc., depending on the length of the y-points.
    So, if we take the same example as above, and leave out the x-points, the diagram will look
    like this:
    '''
    ypoints = np.array([3, 8, 1, 10, 5, 7])

    plt.plot(ypoints)
    plt.show()
def plot5():
    '''
    Markers
    You can use the keyword argument marker to emphasize each point with a specified marker:
    '''
    ypoints = np.array([3, 8, 1, 10])
    '''check Marker Reference
    You can choose any of these markers
    plt.plot(ypoints, 'o:r')  it differentiates from plt.plot(ypoints, marker = '*')
    adding :next to the markers gives it a colour check Color Reference
    checkout Line Reference

    '''
    plt.plot(ypoints,'*:r')
    plt.show()
def plot6():
    ypoints = np.array([3, 8, 1, 10])
    #when you want to increase size of the marker
    plt.plot(ypoints, 'o:r', ms = 20)
    plt.show()

def plot7():
    ypoints = np.array([3, 8, 1, 10])
    ''' noting about the colour of the edgesof the markers refer the colour reference '''
    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
    plt.show()

def plot8():
    ypoints = np.array([3, 8, 1, 10])
    ''' noting about the colour of the inside of the markers refer the colour reference '''
    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r',mfc = 'r')
    plt.show()

def plot9():
    ''' a defined way to use the 140 supported colrs with their codes'''
    ypoints=np.array([3,5,7,2,9])
    plt.plot(ypoints,marker='o',ms =15,mec ='#4CAF50',mfc='#4CAF50')
    plt.show()
plot9()