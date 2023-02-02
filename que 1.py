def pattern(rows):
   for i in range(rows):
        for j in range(i+1):
            print("* ",end="")
        print("\r")
   for i in range(rows):
        for j in range(rows-i-1):
            print("* ",end="")
        print("\r") 
rows = int(input('Enter the number of rows: '))

pattern(rows)