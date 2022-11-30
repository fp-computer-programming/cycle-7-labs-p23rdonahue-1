#author: RED 11/12/22

#creating a function that will find the sum of two numbers - adds the two variables, sets them equal to a new variable, and returns them
def find_sum(num1,num2):
    num_sum = num1 + num2
    return(num_sum)

#creating a variable outside of the function that calls the output of the function when 111 and 222 are input
my_sum = find_sum(313,212)

#printing the newly created variable - which is equal to a specific ouptput of the function
print(my_sum)
#when the whole program is run only the number 333 (the sum) is printed by the last statement