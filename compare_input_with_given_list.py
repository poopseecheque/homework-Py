list_to_compare = [0, 11, '23', 23]
print(list_to_compare)
size = int(input('size: '))
    
list_one = [] #empty so that we could append 2 strings
for i in range(size): #repeasts cycle i times for i values
   temp = int(input(f'{i+1}th value: ')) # we add +1, otherwise it starts with 0
   list_one.append(temp)    #adds i values repeatedly to an empty string

common = [val for val in list_to_compare if val == val in list_one]
print(common)