
# Calculate the average of a list of numbers with unknown length
# List inputs end when adding 0 to the List or pressing enter

def Avg(lst):
    if len(lst) == 0 : return 0
    return sum(lst) / len(lst)

list = []
while True:
    i = input('Add a number to the list, nothing to calculate AVERAGE of all elements: ')
    if len(i)==0: # press enter
        break
    if int(i) == 0: # enter 0
        break
    list.append(int(i))

print('The average of the list is:', Avg(list))
