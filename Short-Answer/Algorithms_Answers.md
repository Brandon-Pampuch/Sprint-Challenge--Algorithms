#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) the running time is linear or O(n) because there is one iterative loop.  The other numbers are 
coefficients that may affect the final run time, but for the purposes of analysis can be ignored.


b) the running time here is O(n^2) because we have a loop inside of a loop. In a sense the loop will
run for each element in the array.  For example, if we had an array of 5 elements each we would run 
the operation 25 times.  5 times or the length of the array for each element of the array (or other 
similar data structure)


c) here again we get O(n) because the base case will determine when the recursion will stop which is
simply a function of what the initial input to the problem is. There are no other 

## Exercise II

# this is a binary search for the the floor 'n'

This is a binary search and is O(log n) complexity.  the more floors you have to search the more 
efficient the algo becomes because it chops half of the search with every iteration.

1.drop an egg from the middle floor of the building
2.if it breaks look at the bottom half of the building
3.if it doesn't break look at the top half of the building
4.half this again by dropping an egg at the middle of whichever part of the building you are at
5.repeat steps one and two on the current half you are looking at
6.once you are checking one floor between two floors you will be able to tell which floor is the highest
7.if that one floor breaks the egg, the last floor is the one below it
8.if that one last floor does not break the egg the answer is that floor
    
    



