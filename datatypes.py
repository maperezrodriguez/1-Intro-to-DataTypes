# Datatypes in Python

# Todo - create a numeric variable

variable = 5.234

# Describe the variable data type

print(type(variable))

# convert / cast the variable into a decimal 2 spaces

variable_new = round(variable,2)

# cast float to integer (whole number)

variable_new = int(variable_new)
print(type(variable_new))

# create a list of numeric values from 1 - 10

list_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print the first 3 elements of the list

print(list_var[:3]

# tell me the number of elements in this list
print(len(list_var))

# print each element in the list created
for i in list_var:
  print(i)

# return the 4 element through the 6th element in this list
print(list_var[3:6])

# put this selected output into a new variable called var_2
var2 = list_var[3:6]

