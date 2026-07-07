

#1.create a list
my_list = [10,20,30,40,50]
print("original list:",my_list)

#2.adding elements
my_list.append(60)
print("after appending 60:",my_list)

#insert an element at a specific position
my_list.insert(2,25)
print("after inserting 25 at index 2:",my_list)


#extend the list with multiple elemnts
my_list.extend([70,80])
print("after extending with [70,80]:",my_list)

#3. removing elemnts
#remove an element by value
my_list.remove(30)
print("after removing 30:",my_list)


#remove an element by index and return it

removed_element = my_list.pop(1)
print("after popping index 1 (removed element is{}):".format(removed_element),my_list)

