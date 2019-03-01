Task solutions for numerical methods labs.

Tasks:  
1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)  
2 ask the user for a number and print its factorial (1p)  
3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)  
4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)  
test your solution properly. Look how it behaves given different input values. (1p)  
5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)  
Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.


0 Use alternative way of reading inputs - using library (0.5p)  
1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)  
2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)  
3 Check if X is divisible by Y (do it in one line of code)  , print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)  
Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.  
4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)  
5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
 it's totally up to your imagination how do you want to amend the figure according to the input number (1p)  
6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5) work for all input values?
 In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)  


1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:  
 - type: circle/rectangle/triangle/rhombus  
 - x & optional y.  
 For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are 
 accordingly the base and the height and for rhombus - diagonals (4p)  
  
2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)  
 The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]  
 Expected output would be 'The first figure (Circle) has larger field'  
3 Test your solutions  


1 Looking at the Euler method above create your own function which takes:
 a (from x' = ax)  
 h - step  
 T time range  
 as an input and plots the solution of a differential equation x' = ax (1p)  
2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)  
2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'  
3 Find a differential equation which represents a process / model (your choice) and implement it using odeint python function (1p)  
4 Look at the example of optimization for exponential function.
 Did you encounter any errors? Where in code do we display the optimal point? Do we minimize or maximize and which function?
 Start your search always from the point (0, -2). (1p)  
5 Create your own 3d function with multiple local optima.
 Create an algorithm which takes an initial point and looks for the closest local optimum (1p)  
 Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)  
 If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).  
 You can, for example, execute your search function multiple times and check if the returned result is what you expected.
 Measure the success / total trials rate (2p).  


To use the requests library you have to install it first. If you have pip and you're using python3 interpreter in your project
 then simply pip3 install requests  
 1 Find another public API with cryptocurrency and compare prices. As an output print:
 "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)  
 2 Use https://randomuser.me API to download a random user data.
 Create and store 100 random users with ids, username, name (first + last name) using this API (2p)  
 3 Prepare a simulation of transactions between these users
 Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
 username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)  
 Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)  
 Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
 Remember to amend user's assets after the transaction. (2p)  
