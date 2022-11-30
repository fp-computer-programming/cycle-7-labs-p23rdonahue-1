#author: RED 11/28/22

#creating a function which finds the lowest number of any given array
def minimum(arr):
    arr.sort()
    return arr[0]

#creating a function which finds the highest number of any given array
def maximum(arr):
    arr.sort()
    return arr[len(arr)-1]

#Creating a function which finds the greatest possible difference
#from the highest and lowest numbers found in the array by the previous two functions
def largest_possible_dif(arr):
    highest = maximum(arr)
    lowest = minimum(arr)
    return(highest-lowest)

print(largest_possible_dif([53,3,21,7,121,4]))