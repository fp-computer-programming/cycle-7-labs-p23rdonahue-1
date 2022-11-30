# Author: RED 11/18/22

def num_sorting(num1,num2,num3,num4,num5,num6,num7,num8):
    #creating a list of the functions inputed numbers
    numbers = [num1,num2,num3,num4,num5,num6,num7,num8]
    #sorting the list from the lowest to highest number and printing the first and last numbers in the list respectively to lowest and highest
    numbers.sort()
    return("The lowest value is "+str(numbers[0])+", and the highest value is "+str(numbers[len(numbers)-1])+".")

#Test Cases for num_sorting (Lab_6-5)
print(num_sorting(7,13,3,8,25,1,0,22) == "The lowest value is 0, and the highest value is 25.")
#result should be true
print(num_sorting(15,30,2,47,59,64,18,-8) == "The lowest value is -8, and the highest value is 64.")
#result should be true
print(num_sorting(1,9,3,8,4,7,5,6) == "The lowest value is 1, and the highest value is 9.")
#result should be true
print(num_sorting(.1,.0001,.001,.0002,.2,.002,.5,.05) == "The lowest value is 0.0001, and the highest value is 0.5.")
#result should be true

def word_sorting(w1,w2,w3,w4,w5):
    words = [w1,w2,w3,w4,w5]
    word_lengths = [len(w1),len(w2),len(w3),len(w4),len(w5)]
    return(words, word_lengths)

#Test Cases for word_sorting (Lab_6-6)
print(word_sorting("The","Bird","Flew","Really","High") == (['The', 'Bird', 'Flew', 'Really', 'High'], [3, 4, 4, 6, 4]))
#result should be true
print(word_sorting("Sherlock","Holmes","A","Murder","Mystery") == (['Sherlock', 'Holmes', 'A', 'Murder', 'Mystery'], [8, 6, 1, 6, 7]))
#result should be true
print(word_sorting("A","Very","Tall","Blue","Jay") == (['A', 'Very', 'Tall', 'Blue', 'Jay'], [1, 4, 4, 4, 3]))
#result should be true
print(word_sorting("To","Begin","A","Journey","Through") == (['To', 'Begin', 'A', 'Journey', 'Through'], [2, 5, 1, 7, 7]))
#result should be true

def num_doubles(num1,num2,num3):
    nums = [int(num1)*2,int(num2)*2,int(num3)*2]
    return(nums)

#Test Cases for num_doubles (Lab_6-7)
print(num_doubles(2,4,6) == [4,8,12])
#result should be true
print(num_doubles(10,20,30) == [20,40,60])
#result should be true
print(num_doubles(5,15,25) == [10,30,50])
#result should be true
print(num_doubles(-2,-4,-6) == [-4,-8,-12])
#result should be true

def num_even_odd(num1,num2,num3):
    nums = [int(num1),int(num2),int(num3)]
    if(nums[0]%2 == 0 and nums[1]%2 == 0 and nums[2]%2 == 0):
        return("even")
    elif(nums[0]%2 == 1 and nums[1]%2 == 1 and nums[2]%2 == 1):
        return("odd")
    else:
        return("mixed")

#Test Cases for num_even_odd (Lab_6-8)
print(num_even_odd(1,2,3) == "mixed")
print(num_even_odd(2,4,6) == "even")
print(num_even_odd(3,7,13) == "odd")
print(num_even_odd(64,13,21) == "mixed")