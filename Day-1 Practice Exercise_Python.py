#!/usr/bin/env python
# coding: utf-8

# # 1 Manipulate using a list

# In[1]:


lst = [20,50,'prakash','mphasis']
lst


# In[2]:


lst.append(36) #Adding the new element
lst


# In[5]:


lst.reverse() #Reverse the list
lst


# In[6]:


lst*2 # list of elements multiple times


# In[12]:


lst2 = [30,60,70,10,2] #concatenate two lists
final_lst = lst + lst2
final_lst


# In[14]:


lst2.sort() # sorting the elements in the lsit
lst2


# # 2 Write a program to do in the Tuples

# In[16]:


tup = (10,20,'praksh',48) # tuple was created
type(tup) 


# In[21]:


lst1 = [20,50,601,46,34,'praksh'] #manipulating the tuple 
my_tuple = tuple(lst1)
print(my_tuple)


# In[44]:


lst1.reverse()
my_tuple= tuple(lst1)
my_tuple


# In[61]:


lst_new = [10,'prakas',56,78,43,2]#Display multiple times
n = lst_new*2
new_Tuple=tuple(n)
new_Tuple


# In[65]:


List1= [10,4,80,67,89,43,2] #concatenate two tuples
np = List1 + lst_new
my_Tuple = tuple(np)
my_Tuple


# In[68]:


List1.sort() #sorting the list and type casting into tuple
my_Tuple1 = tuple(List1)
my_Tuple1


# # 3 Write aprogram to implement the following using list

# In[69]:


list_integers = [2,3,5,6,7,9,8,4,1,10] #created a list with minimum Ten Integers
list_integers


# In[71]:


list_integers[-1] #last number in the list 


# In[72]:


list_integers[0:4] # for display 0 to 4 indexing values in list


# In[73]:


list_integers[2:] # for display 2 to end of the indexing values in list


# In[74]:


list_integers[:6] # defaulty it took 0 to 6 of the indexing values in list


# # 4 write a python program for tuple

# In[78]:


t0=(10,50,20,40,30) #As mention to create a tuple by using this values
t0


# In[79]:


t0[:2] #To display 10 and 50 from tuple 


# In[80]:


len(t0) #To display length


# In[81]:


min(t0) #To display minimum values


# In[82]:


sum(t0) #to sum of all elements in the tuple


# In[83]:


t0*2 #to displaythe same tuple multiple times


# # 5 write a python program

# In[84]:


st = 'prakash' #creating the string value
st


# In[85]:


len(st) #length of string


# In[90]:


st[::-1] #reverse the string


# In[97]:


st*2 #multiple time of string


# In[101]:


st2 = 'nani' #concatenation of two strings
st1 = st + st2 
st1


# In[102]:


Str1 = "South India" #using slicing to display india
Str1[6:]


# # 6 perform the following

# In[105]:


dic = {'f_name':'prakash','l_name':'nani','age':'22'} #creating the dictionary
dic



# In[106]:


dic.values() #Accessing the values


# In[107]:


dic.update({'age':'23'}) #Updating the dictionary file
dic


# In[124]:


dic.clear()
dic


# # 7 Python program to insert a number to any position in the list

# In[128]:


List_name = [20,6,80,65,45,3,89,3,2,5,6,78] 
List_name.insert(2,35) #By using insert method i added 35 in the 2 index number
List_name


# # 8 python program to delete an element from list by index

# In[131]:


Listname = [25,9,6,5,4,7,8,23,2,4,6] #creating list 
Listname.remove(6) # the number six was deleted in the index
Listname


# # 9 write a program to display 1 to 100

# In[136]:


n=1
while n <= 100:
    print(n,end=" ")
    n = n + 1


# # 10 write a program to print sum of all iteams in tuple

# In[138]:


tup = (10,70,5,4,7,8) #sum of all values in the tuple
sum(tup)


# # 11 creating dictionary containing three lambda functions square, cube and square root

# In[162]:


s=int(input("Enter the Square value"))
c=int(input("Enter the cube value"))
sq=int(input("Enter the Square Root"))
dict1={'Square':s,'Cube':c,'SquareRoot':sq}


# In[163]:


dict1 #the input values are stored


# In[164]:


print(sum(dict1.values())) #sum of all the thre lambda function



# # 12 A list of words is given find words from the list that have their second character in upper case

# In[172]:


ls = ['hello','Dear','hOw','ARe','You'] #find out second character capital letter
ls1=[]
for i in ls:
    
    if i[1].isupper():
        ls1.append(i)
ls1


# In[ ]:


13 


# In[ ]:





# In[ ]:





# In[ ]:





#    # Control Structures

# # 1 write a program to find first N prim numbers

# In[183]:


i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1


# # 2 write the python code that calculates the salary of an employee

# In[184]:


sa = int(input("Enter the SA"))
hra = int(input("Enter the HRA"))
ta = int(input("Enter the TA"))
da = int(input("Enter the DA"))
Gross_salary=sa+hra+ta+da
deduct = 0.1 * Gross_salary
total_salary = Gross_salary - deduct
total_salary


# # 3 write a python program to search for string in the given list

# In[191]:


List_one = ['prakash','nani','surya','king','pawan']
n = input("enter the name")
for i in List_one:
    if(i == n):
        print("The name Matched")
        break
    else:
        print("The name wa not matched")


# # 4 write a python function that accepts a string and calculates the number of upper case-case letters and lower-case letters

# In[ ]:





# In[ ]:





# In[ ]:





# # 5 Program to display the sum of odd numbers and even numbers that fall between 12 and 37

# In[199]:


n=0
m=0
for i in range(12,38):
    if(i%2==0):
        n=n+i
print("The sum of even numbers {}".format(n))
for j in range(12,38):
    if(j%2!=0):
        m=m+j
print("The sum of odd numbers {}".format(m))


# # 6 write a program to print a table

# In[203]:


n=2
m=0
for i in range(1,11):
    m=n*i
    print("{} * {} = {}".format(n,i,m))
    
    


# # 7 write a program to sum the first 10 prime numbers

# In[204]:


i = 1
m=0
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
       
        print(i)
    else:
        k = k - 1

    i = i + 1


# In[ ]:


8


# In[ ]:





# In[ ]:





# In[ ]:


9


# In[ ]:





# In[ ]:


10


# In[ ]:





# In[ ]:


11


# In[ ]:





# In[ ]:





# In[ ]:


12


# In[ ]:





# In[ ]:


13


# In[ ]:





# In[ ]:


14


# In[ ]:





# In[ ]:


15


# In[ ]:





# In[ ]:


16


# In[ ]:





# # 17 print a pattern

# In[205]:


n=int(input("enter number"))
for i in range(1,n+1):
    print("*"*i)


# In[ ]:




