''' Before runing this program make sure to install
	1.Python.
	2.matplotlib using 'pip install matplotlib' command.
	By
	Prapanna Bista.
	Section: B
	3rd semester ASCOL College BSc CSIT.
'''


import math, random, statistics, string
import matplotlib.pyplot as plt 


def main():
	distance_lists = []
	paths = int(input("Enter number of paths. "))
	for path in range(1,paths+1):
		steps = 1000 #We need to move 1000 steps but feel free to change according to your choice of steps.
		x,y = 0,0 #let's starting point be origin.
		x,y,x_axis,y_axis = randomWalk(steps,x,y)
		distance_lists.append(calculateDistance(x,y))
		plt.plot(x_axis, y_axis , label = "path "+str(path))
		plt.legend()
	    # plt.plot(x_axis,y_axis, color='black',marker='o', markerfacecolor='white',markersize=2)
	print("The maximum displacement = "+str(max(distance_lists)))
	print("The average displacement = "+str(statistics.mean(distance_lists)))
	plt.xlabel('x-axis')
	plt.ylabel('y-axis')
	plt.title('Random walk graphical visualization By Prapanna Bista \n Maximum Displacement = '+str(round(max(distance_lists),2))+', Average Displacement ='+str(round(statistics.mean(distance_lists),2)))
	plt.show()


def calculateDistance(x,y):
	return math.sqrt(x*x+y*y)

def randomWalk(steps,x,y):
    x_axis = [x]	#Initializing list of x co-ordinates
    y_axis = [y]
    for step in range(steps):
        direction = random.randint(0,3)
        # (North East South West) = ( 0 1 2 3 ) 

        if direction == 0:
            x = x-1
            x_axis.append(x)
            y_axis.append(y)
            
        elif direction == 1:
            y = y+1
            x_axis.append(x)
            y_axis.append(y)

        elif direction == 2:
            x = x+1
            x_axis.append(x)
            y_axis.append(y)

        else:
            y = y-1
            x_axis.append(x)
            y_axis.append(y)

    return x,y,x_axis,y_axis

main()
