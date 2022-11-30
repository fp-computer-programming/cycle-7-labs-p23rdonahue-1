# Author: RED 11/18/22

#creating a function that will find the sum of two numbers - adds the two variables, sets them equal to a new variable, and returns them
def find_sum(num1,num2):
    num_sum = num1 + num2
    return(num_sum)

#creating a variable outside of the function that calls the output of the function when 111 and 222 are input
my_sum = find_sum(111,222)

#printing the newly created variable - which is equal to a specific ouptput of the function
print(my_sum)
#when the whole program is run only the number 333 (the sum) is printed by the last statement

#Test Cases
print(find_sum(21,17) == 38)
#21 + 17 should equal 38
print(find_sum(35,-12) == 23)
#35 + (-17) should equal 23
print(find_sum(10000,-10001) == -1)
#10000 + (-10001) should equal -1
print(find_sum(.1,.01) == .11)
#.1 + .01 should equal .11