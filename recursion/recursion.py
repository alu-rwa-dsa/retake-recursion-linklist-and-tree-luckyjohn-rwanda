def CheckDigit(arr, i, countodd, counteven):
   # If current index is invalid
   if i < 0:
       # Print the message
       if counteven > countodd:
           print("Your input has more even digits than odd")
       elif counteven < countodd:
           print("Your input has more odd digits than even")
       else:
           print("Your input has equal even and odd digits")

       return

   # If current element is 0
   if arr[i] == 0:
       counteven += 1

   # If current element is even
   if (arr[i]) % 2 == 0:
       # Add it to the number of odd nbrs
       counteven += 1

   # If current element is odd
   else:
       countodd += 1

   # Recursive call for the next element
   CheckDigit(arr, i - 1, countodd, counteven)

# Take user input
userinput = input("Enter any given digit: ")

# Check if the user input is a digit
if userinput.isdigit():
  
   # split the digit into an integer array of numbers
   arr = [int(i) for i in str(userinput)]
   n = len(arr)
   countodd = 0
   counteven = 0

   CheckDigit(arr, n - 1, countodd, counteven)

else:
   print("Your input is not a full digit")
