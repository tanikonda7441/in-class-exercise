input_String = 'The quick Brow Fox'
input_String =  input_String.replace(" ","")
upper_case = []
lower_case = []
for i in input_String:
    if i.islower():
        lower_case.append(i)
    else:
        upper_case.append(i)
print("No. of Upper-case characters:" + str(len(upper_case)))
print("No. of Lower-case Characters:"+ str(len(lower_case)))
    