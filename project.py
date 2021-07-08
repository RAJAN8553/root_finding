# -*- coding: utf-8 -*-
"""
@author: RAJAN
"""

import time
from math import sin as sin
from math import cos as cos
from math import exp as exp
from math import log as log
import sympy as sym
#import matplotlib.pyplot as plt
    
def graph(ls):
    plt.plot(*zip(*sorted(ls.items())))
    # sorted() sorted by key, return a list of tuples
    # Zip() unpack a list of pairs into two tuples
    # items() Function show keys and values
    ax = plt.gca() #ax = gca returns the current axes (or standalone visualization)
    ax.spines['left'].set_position('center')
    #Spines are the lines connecting the axis tick marks and noting the boundaries of the data area.
    ax.spines['right'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_position('center')
    ax.set_ylim([-20, 20])
    #ylim() Function. The ylim() function in pyplot module of
    #matplotlib library is used to get or set the y-limits of the current axes
    plt.title('Numerical Methods ')
    plt.show()
def function(): 
    global fu
    fu = input("Enter Your Function f(x) : ")
    return fu;
def f(fun,x):
    fu = eval(str(fun))
    return fu


def line(x):
    print("_"*x)
    
# Implementing Bisection Method
def bisection(x1,x2,e,fu):
    global count_b;
    count_b += 1;
    
    line(80)
    print('\n\t\t*** BISECTION METHOD IMPLEMENTATION ***')
    line(80)
    n= 1
    ls = dict()
    start_time = time.perf_counter() # convert to mili sec.
    if f(fu,x1) * f(fu,x2) < 0.0:
        
        print("{0:<5} {1:<12.4} {2:<12} {3:<12.4} {4:<12} {5:<12.4} {6:<12}".format('n','x1','f(x1)','x2','f(x2)','x3','f(x3)'))
        condition = True
  
        while condition:
            x3 = (x2 + x1)/2
            line(80)
            print("{0:<5d} {1:<12.4f} {2:<12.4f} {3:<12.4f} {4:<12.4f} {5:<12.4f} {6:<12.4f}".format(n,x1,f(fu,x1),x2,f(fu,x2),x3,f(fu,x3)))
            n = n + 1
            if f(fu,x1) * f(fu,x3) < 0:
                x2 = x3
            else:
                x1 = x3
            if f(fu,x1) * f(fu,x3) == 0:
                condition = False
                
            ls.update({x3:f(fu,x3)})
            condition = abs(f(fu,x3)) > e
        
        line(80)  
        print('Root Of An Equation is: %0.4f' % x3 )
        print('Number of iteration : %d' % (n-1))
    else:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    
    end_time = time.perf_counter()
    diff = end_time - start_time
    print(f"Execution Time is : {diff:0.6f} seconds")
    
    print("Do you want a Graphical Representation : ")
    temp = int(input("Enter Your Choice :(1/0)"))
    
    if(temp==1):
        graph(ls)
    else:
        pass
    return diff
    # Implementing Secant Method
def secant_method(x1, x2, e ,fu):
    global count_s;
    ls = dict()
    count_s += 1;
    n = 1;
    line(80)
    print('\n\t\t*** SECANT METHOD IMPLEMENTATION ***')
    line(80)
    
    start_time = time.perf_counter()

    if (f(fu,x1) * f(fu,x2) < 0.0): 
        condition = True
        print("{0:<5} {1:<12.4} {2:<12} {3:<12.4} {4:<12} {5:<12.4} {6:<12}".format('n','x1','f(x1)','x2','f(x2)','x3','f(x3)'))     
        while condition:
            if f(fu,x1) == f(fu,x2):
                print('Divide by zero error!')
                break
            x3 = ((x1 * f(fu,x2) - x2 * f(fu,x1)) / (f(fu,x2) - f(fu,x1)));  #secand Method Formula
            
            line(80)
            print("{0:<5d} {1:<12.4f} {2:<12.4f} {3:<12.4f} {4:<12.4f} {5:<12.4f} {6:<12.4f}".format(n,x1,f(fu,x1),x2,f(fu,x2),x3,f(fu,x3)))
              
            x1 = x2;  
            x2 = x3;  
            n = n+1;  
            
            condition = abs(f(fu,x2)) > e  
            ls.update({x3:f(fu,x3)})
    
        line(80)  
        print('Root Of An Equation is : %0.4f' % x3)
        print('Number of iteration : %d' % (n-1))  
    else:
        print("This Not Possible")  

    end_time = time.perf_counter()
    diff=end_time - start_time
    print(f"Execution Time is : {diff:0.6f} seconds")
    print("Do you want a Graphical Representation : ")
    temp = int(input("Enter Your Choice :(1/0)"))
            
    if(temp==1):
        graph(ls)
    else:
        print("You Don't Need To Watch Graphical Representation ")
    
    return diff

# Implementing False Position Method
def falsePosition(x1,x2,e,fu):
    global count_f;
    count_f += 1;
    n = 1
    line(80)
    print('\n\t\t*** FALSE POSITION METHOD IMPLEMENTATION ***')
    line(80)
    ls = dict()
    start_time = time.perf_counter()

    if f(fu,x1) * f(fu,x2) < 0.0:
        
        condition = True
            
        print("{0:<5} {1:<12.4} {2:<12} {3:<12.4} {4:<12} {5:<12.4} {6:<12}".format('n','x1','f(x1)','x2','f(x2)','x3','f(x3)'))

        while condition:
            x3 = ((x1 * f(fu,x2)) - (x2 * f(fu,x1))) / (f(fu,x2) - f(fu,x1))
            ls.update({x3:f(fu,x3)})
            print("_"*80)    
            print("{0:<5d} {1:<12.4f} {2:<12.4f} {3:<12.4f} {4:<12.4f} {5:<12.4f} {6:<12.4f}".format(n,x1,f(fu,x1),x2,f(fu,x2),x3,f(fu,x3)))
            if f(fu,x1) * f(fu,x3) < 0:
                x2 = x3
            else:
                x1 = x3

            n = n+ 1
            condition = (abs(f(fu,x3)) > e)
            
            
        line(80)
        print('Root Of An Equation is : %0.4f' % x3)
        print('Number of iteration : %d' % (n-1))

    else:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    
    end_time = time.perf_counter()
    diff=end_time - start_time
    print(f"Execution Time is : {diff:0.6f} seconds")
    print("Do you want a Graphical Representation : ")
    temp = int(input("Enter Your Choice :(1/0)"))
            
    if(temp==1):
        graph(ls)
    else:
        print("You Don't Need To Watch Graphical Representation ")
    
    return diff
# Implementing Newton Raphson Method
   
def g(x):
    global fu
    dif = sym.diff(fu)
    fx = eval(str(dif))
    return fx


def newtonRaphson(x1,e,fu):
    global count_n;
    count_n += 1;
    line(80)
    print('\n\t\t*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    line(80)
    n = 1
    ls = dict()
    start_time = time.perf_counter()

    condition = True
    print("{0:<5} {1:<12} {2:<12} {3:<12} {4:<12}".format('n','x1','f(x1)','x2','f(x2)'))
    while condition:
        x2 = x1 - f(fu,x1)/g(x1)
        ls.update({x2:f(fu,x2)})
        line(80)
        print("{0:<5d} {1:<12.4f} {2:<12.4f} {3:<12.4f} {4:<12.4f}".format(n,x1,f(fu,x1),x2,f(fu,x2)))  
        x1 = x2
        n = n + 1
        condition = abs(f(fu,x2)) > e
        
    line(80)  
    print('Root Of An Equation is : %0.4f' % x2)
    print('Number of iteration : %d' % (n-1))
    print("_"*80)    

    end_time = time.perf_counter()
    diff=end_time - start_time
    print(f"Execution Time is : {diff:0.6f} seconds")
    print("Do you want a Graphical Representation : ")
    temp = int(input("Enter Your Choice :(1/0)"))
            
    if(temp==1):
        graph(ls)
    else:
        print("You Don't Need To Watch Graphical Representation ")
    
    return diff
   
""" 
Main Body of Program
"""
line(80)
print("*"*80)
print ("\t\t\t\t\t\t Find the root of an eqation")
line(80)
print("*"*80)

fu=function()
x1=int(input( "Enter First Value X1  : "))
x2=int(input("Enter Second Value X2 : "))
ex = float (input("Enter The Number Of Significunt digit you want like(0.0001): "))
    
total_time_bisection=0
total_time_flaseposition=0
total_time_secant=0
total_time_newton=0
count_b = 0 
count_f =0 
count_s =0 
count_n = 0
i = 1
while(i<7):
    line(80)
    print ("*"*80)
    print ("Enter Your Choice ")
    print ("1. Bisection Method  ")
    print ("2. False Position    ")
    print ("3. Secant Method   ")
    print ("4. Newton Raphson Method   ")
    print ("5. Want new coefficient ")
    print ("6. Avarage Time Taken By each Method")
    print ("7. Exit ")
    i=int (input("Enter Your Choice :"))
    line(80)
    print ("*"*80)
    if(i == 1):
        tb= bisection(x1,x2,ex,fu)
        total_time_bisection+=tb
    elif(i == 2):
        tf= falsePosition(x1,x2,ex,fu)
        total_time_flaseposition+=tf
    elif(i == 3):
        ts= secant_method(x1,x2,ex,fu)
        total_time_secant+=ts
    elif(i == 4):
        tn= newtonRaphson(x1,ex,fu)
        total_time_newton+=tn
    elif(i == 5):
        fu = function()
        x1=int(input( "\nEnter First Value X1  : "))
        x2=int(input("Enter Second Value X2 : "))
        e = float (input("Enter The Number Of Significunt digit you want like(4=0.0001): "))
    elif(i == 6):
        line(80)
        print("*"*80)
        if(count_b != 0):
            print("Avrage Time which Biesction Method Take      : %.5f" % (total_time_bisection/count_b)   )
        if(count_f != 0):
            print("Avrage Time which Flase Position Method Take : %.5f " % (total_time_flaseposition/count_f)  )
        if(count_s != 0):
            print("Avrage Time which Secant Method Take         : %.5f " % (total_time_secant/count_s)   )
        if(count_n != 0):
            print("Avrage Time which Newton Method Take         : %.5f " % (total_time_newton/count_n))
        if(count_n == 0 and count_b == 0 and count_s == 0 and count_f == 0):
            print("Please run minimum 1 times to see all method output : ")
        
