############
## Day: 3 ##
############

#1. Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

#Checks if the athlete name has 't' in any of the sub-lists. 
for athlete_list in athletes:
    for athlete in athlete_list:
        if 't' in athlete:
            t.append(athlete)
        else:
            other.append(athlete)

#####################################################

#2. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst. Use 'map' function to acheive this. 

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map(lambda element: element*2, lst)

######################################################

#3. Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter. use 'filter' function to acheive this. 

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter(lambda element:'w' in element, lst_check))

######################################################

#4. Use list comprehension to create a list called lst2 that doubles each element in the list, lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [element*2 for element in lst]

######################################################

