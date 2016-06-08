# Grade: 12.5 / 15
# This grade applies to the whole assignment, not just this part. Assignments should be completed in one file unless otherwise stated.

#Radhika PC
#5/25/2016
#Homework2
numbers = [22,90,0,-10,3,22, 48]
#display th enumber of elements in the list
# TA-COMMENT: (-0.5) The question asks for the number of elements in the list (not the list itself). We were looking for len(numbers)

print(numbers)

#display the 4th elements
print("The 4th element is", numbers[3])
#Display the sum of the 2nd and 4th element of the list.
print("The sum of 2nd and 4th element is", numbers[1] + numbers[3])
#Display the 2nd-largest value in the list.
sorted_numbers = sorted(numbers)
print("The second largest number is", sorted_numbers[5])

# TA-COMMENT: There is a programmatic way to display the second largest value in a list (other than calling it by its index). For example: numbers_sorted[(len(numbers_sorted) - 2)] OR: numbers_sorted[-2].

#Display the last element of the original unsorted list
print("The last element of the original list is", numbers[6])
# TA-COMMENT: Same comment applies -- numbers[-1] is the most efficient way.


#Sum the result of each of the numbers divided by two.
new = 0
sum = 0
for i in numbers:
    new = i / 2
    sum = sum + new
print("The sum is", sum)

# TA-COMMENT: This would also work:
sum = 0
for i in numbers:
    sum = sum + (i / 2)
print(sum)

# question no:6
#For each number, display a number:
for number in numbers:
    print(number)
#if your original number is less than 10, multiply it by thirty.
for number in numbers:
    if number < 10:
        new_num= number * 30
        print("If original number is less than 10, this is the answer", new_num)
#If it's ALSO (less than ten and even I assume) even, add six
        if number%2 ==0:
            new_new_no = new_num + 6
            print("If the number is less than 10 and an even number, the result is", new_new_no)
# If it's greater than 50 subtract ten.
    if number > 50:
        x_no = number - 50
        print("If the number is greater than 50, the result is", x_no)
# If it's not negative ten, subtract one
    if number !=-10:
        xy_no = number - 1
        print("if the number is not -10, then the result is ", xy_no)


# TA-COMMENT: (-1) Each number should be only be printed once. Though the logic of your if-statements are correct, you switch the name of the variable where you're saving the newly calculated number. This leads to their being multiple results for each original number and the final calculated number to be incorrect (some numbers should go through multiple conditions successively). Let me know if you have any questions about this!
