#1. What is printed by the following statements?

alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)

#Ans: [10]

#2. Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = zip(species,population)

endangered = [species for species,population in pop_info if population < 2500]

#3. if resp is a Response object returned by a call to requests.get(), which of the following is a way to extract the contents into a python dictionary or list?

#A. resp.json() or json.loads(resp.text)