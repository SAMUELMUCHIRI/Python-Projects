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

def plot10():
    # The function is for formatting the nature of the graph line
    # basically looking at the references there are two options 
    #dotted or dashed
    ypoints=np.array([1,4,2,6,7,9])
    plt.plot(ypoints,linestyle= "dotted")
    #line stye can be shortformed as ls and dotted as : full colons,dashed as a pair of dashes
    plt.show()

def plot11():
    ''' the function contains syntax for line editing , in that referring to its width colour 
    or even adding multiple lines '''
    ypoints=np.array([1,4,2,6,7,9])
    ypoints2=np.array([3,5,7,2,9])
    #here you can add multiple lines as shown below
    plt.plot(ypoints,color="red")
    #You can also adjust the line width as seeen
    plt.plot(ypoints2,color="green",linewidth="20")
    plt.show()
def plot12():
    ''' labeling axis is important
    and also including the title '''
    #first considering axis
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    plt.plot(x, y)
    #adding the title and specifying its location by adding loc
    plt.title("Sports Watch Data",loc='left')
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    plt.show()
def plot13():
    ''' labeling axis is important
    and also including the title '''
    #first considering axis
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    plt.plot(x, y)
    #adding the title and specifying its location by adding loc
    plt.title("Sports Watch Data",loc='left')
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    
    #show grid
    plt.grid()

    plt.show()
def plot14():
    #the function clearly depicts how to specify which grid lines are to be shown
    x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
    y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

    plt.plot(x, y)
    #adding the title and specifying its location by adding loc
    plt.title("Sports Watch Data",loc='left')
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    
    #show grid on x axis
    #  also getting creative with the grid by adding line patterns and line size and color 
    plt.grid(color='green',linestyle=':',linewidth=0.5)

    plt.show()
def plot14():
    x = np.linspace(0, 2, 100)  # Sample data.

    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, x, label='linear')  # Plot some data on the axes.
    ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
    ax.plot(x, x**3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()
plot14()