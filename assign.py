 #assigns interger values and displays both assigned values
a = 8
b = 4
print ('Assigned Values:\t\t','a =',a,'\tb=', b)
 #Placing the \t in front of the b variable adds a space
 #between assignments

 #Next we are adding and assigning a new value to the
 #first variable.
a += b #here we assign the value of 'a'. Below we call this new value. Same as regular variable assignment.
print('Add & Assign:\t\t', 'a =', a , '(8 += 4)')

 #Subtracts and assigns a new value to the first variable.
 #Then multiply and assign a value to the first variable.
a-=b
print('Subtract and Assign:\t', 'a =', a , '(12 - 4)')

a*=b
print ('Multiply and Assign:\t', 'a=', a, '(8 * 4)') 
 #Remember the value of the Subtraction problem was assign to 'a' prior to multiplying.
 #Divide and assign a new value to first variable.
 #Next, modulus and assign a value to the first variable.
a /= b
print('Divide and Assign:\t', 'a =', a , '(32/4 )')

a %= b
print('Modulus and Assign:\t', 'a =', a , '(8 % 4)')
 