#1. Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.

animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1 = animals[1][0]

###########################################################################

#2. Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'],
          'diving': ['springboard', 'platform', 'synchronized'],
          'track': ['sprint', 'distance', 'jumps', 'throws'],
          'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'],
                         'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]

# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']

# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]

#3. nested-9-1: Because we can only write strings into a file, if we wanted to convert a dictionary d into a json-formatted string so that we could store it in a file, what would we use?

#Ans.
json.dumps(d) #dumps turns a list or dictionary into a json-formatted string

##########################################################################

#4.Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = [] #Created to hold names of athletes containing the letter 't'
other = [] #Created to hold names of athletes not containing the letter 't'

for athlete_list in athletes:
    for athlete in athlete_list:
        if 't' in athlete:
            t.append(athlete)
        else:
            other.append(athlete)

###########################################################################
