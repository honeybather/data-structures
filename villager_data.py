"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
#goal is to take species (second item per line) and retun a unique list
# method 1- itterate through each line, pull index 1, and save as set to elim dups
# method 2 - new_set = {expression for item in old_list if condition} -> want to become an array of lines
    # file = filename.split
    # species = set(line[1] for line in file) 
    species = set()
    for line in filename:
        parts = line.split("|")
        species.add(parts[1])
    

    return species
# print(all_species(open('villagers.csv')))      



"""Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

def get_villagers_by_species(filename, search_string="All"):
    villagers = [] 
    file = open(filename)
    for line in file:
        array_line_part = line.split("|") #array of line parts "Teddy", "Bear", "Jock|Fitness|No pain, no gain!""
        name = array_line_part[0]
        species = array_line_part[1]
        if search_string == "All":
            villagers.append(name)
        else: 
            if species == search_string:
                villagers.append(name)
    
            #only select the ones that match 

    return sorted(villagers)
print(get_villagers_by_species('villagers.csv','Bear'))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.
    [[fashion, [name, name name]], music[name, name, name]]

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # method 1 -> collect all hobbies -> make each one an array
        # loop through whole list again, and add names where hobbies match
    # method 2 -> if a list exists with [0] being hobby, add name to that hobby, 
                # if not, make new list, add name
    # Method 3 - we know there are 6, so we will build the results based on index of known hobbies 
        #assign fitness = index 0, 

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code





# git remote add https://github.com/honeybather/data-structures.git 
https://github.com/honeybather/data-structures.git