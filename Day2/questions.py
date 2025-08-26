#Question 1: Create a list of 10 numbers and print it.

# li=[]

# for i in range(10):
#     li.append(int(input("Enter data:")))
# print(li)   
    


#Question 2: Find the length of a list without using len().
# my_list = [1, 2, 3, 4, 5]
# count = 0
# for item in my_list:
#         count += 1

# print(count)

#Question 3 : Access the first, middle, and last element of a list.

# li=[5,1,2,54]
# print(li[0])

# print(li[-1])

# print(li[len(li)//2])

#Question 4 : Print a list in reverse order without using reverse() or slicing.

# li=[5,4,5,83,12]

#Question 5: Find the maximum and minimum element from a list without using max()/min().

# li = [1,2,4,5,6,7,8,78,12,44]

# li.sort()
# print(li)
# print(li[0])
# print(li[-1])

#Question 6: Calculate the sum of all numbers in a list.

# li =  [1,2,4,5,6,7,8,78,12,44]
# sum=0
# for i in li:
#     i+=i
# print("sum:",i)


#Question 7: Count how many times a specific number appears in a list.
# li =  [1,2,4,5,6,7,8,78,12,44,2,2]

# cnt=int(input("Enter the data which you want to find:"))

# print(li.count(cnt))


# Question 8 : Remove all occurrences of a specific number from a list.

    
# li =  [1,2,4,5,6,7,8,78,12,44,2,2]

# cnt=int(input("Enter the data which you want to remove:"))

# print(li.remove(cnt))



#Question 9: Remove duplicates from a list.



# li =  [1,2,4,5,6,7,8,78,12,44,2,2]

# print(list(set(li)))

#Question 10: Check if a list is empty or not.

li=[]

if li:
    print("True")
else:
    print("False")