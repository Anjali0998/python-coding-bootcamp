def calculator():
   n1=int(input('Enter the first number'))
   n2=int(input('Enter the second number'))
   op=input('Enter any operation +,-,/,*')

   if (op=='+'):
      print(n1+n2)
   elif op=='-':
      print(n1-n2)
   elif op=='/':
      print(n1/n2)
   elif op=='*':
      print(n1*n2)
   else:
      print('Wrong input(s)')
   
   choice=input('do you want to continue Y/N:')
   if choice=='Y':
      calculator()
   else:
      print('bye')

calculator()
