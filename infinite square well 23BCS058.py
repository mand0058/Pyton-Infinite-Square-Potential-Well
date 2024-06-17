#physics assignment
#Name=Mandeep Kumar
#Branch = Computer Science And Engineering
#roll No= 23BCS8058



#python program for plotting the graph of a infinite square well

import matplotlib.pyplot as plt    #Importing  matplotlib.pylot () 
                                   # Matlab is a python library whicgh is used to plot the graphs
import numpy as np                 # Importing numpy (numpy is a python library whicch contains all the functions such as sin(x), cos(x)
pi = np.pi
a = float(input("Enter value of a: "))   #Taking The Value of a from user


deep = np.linspace(0,a,1000)          #creating array of thousand values between 0 and a ( The more values we take between 0 and a the smoother is the graph
A = (2/a)**(0.5)                      #in simple words these are the values of x
                                      

def wavefunction(n,x) :          # creating a function of wavefunction  
    wf = (A*np.sin(n*pi*x/a))**2
    return wf
    
    

man1 = wavefunction(1,deep)         #storing the values of wavefunction in different variables to wrt different 
man2 = wavefunction(2,deep)        #values of n ranging from (1 to 5) and the values of x are taken from the above list deep
man3 = wavefunction(3,deep)
man4 = wavefunction(4,deep)
man5 = wavefunction(5,deep)


figure, axis = plt.subplots(nrows=5, figsize=(12, 15))  #this figsize controls the width and height of graph plots

axis[0].plot(deep,man1 , label="n=1")   #this function plots the graph
axis[0].axhline(y = 0, color = 'r')     #this prints axis line and gives colour also
axis[0].grid()                          #this line prints the grid
axis[0].legend()                        #this line helps in labelling of graph

axis[1].plot(deep,man2 , label="n=2")
axis[1].legend()
axis[1].grid()
axis[1].axhline(y = 0, color = 'r')

axis[2].plot(deep,man3 , label="n=3")
axis[2].legend()
axis[2].grid()
axis[2].axhline(y = 0, color = 'r')

axis[3].plot(deep,man4 , label="n=4")
axis[3].legend()
axis[3].grid()
axis[3].axhline(y = 0, color = 'r')

axis[4].plot(deep,man5 , label="n=5")
axis[4].legend()
axis[4].grid()
axis[4].axhline(y = 0, color = 'r')

plt.show()               # used to display the graphs 