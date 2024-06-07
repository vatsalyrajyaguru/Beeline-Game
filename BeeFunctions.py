import csv

# load flower txt file
def load_flower_list():
    flower_dict = {}
    while True:
        try:
            filename = input("Enter the name of the file containing the flower to pollen mapping: ")
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip().split(',')
                    flower_dict[line[0]] = (line[1], int(line[2]))
                return flower_dict
        except FileNotFoundError:
            print("File not found. Please provide a valid filename.")

# load csv file
def create_field(flower_dict):
    field = []
    while True:
        try:
            filename = input("Enter the name of the file containing the field: ")
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    field.append(row)
                return field
        except FileNotFoundError:
            print("File not found. Please provide a valid filename.")

#  make a copy of a field
def copy_field(field):
    return [[' ' if char in ['H', 'P', 'U'] else char for char in row] for row in field]

#  print the field
def print_field(field):
    print("  " + " ".join(str(i) for i in range(len(field[0]))))
    for i, row in enumerate(field):
        print(i, " ".join(row))

#  game introductory information
def game_intro(flower_dict, num_scouts, num_workers, pollen_needed):
    print("Welcome to Beeline!")
    print("You play as the queen bee trying to produce honey from the pollen of flowers.")
    print("You have two kinds of bees, scouts and workers.")
    print("Scouts fly to a location and reveal the flowers in a 3x3 grid centered on that location.")
    print("Workers fly to a location, reveal the flowers in a 3x3 grid centered on that location, and harvest pollen from any unharvested flowers.")
    print("You only have", num_scouts, "scout bees and", num_workers, "worker bees to harvest", pollen_needed, "amount of pollen.")
    print("A bee can only be sent out once, and a flower can only be harvested once.")
    print("Be careful of pitcher plants, they will trap your bees!")
    print("Flower Types and Pollen Counts:")
    for key, value in flower_dict.items():
        print(f"{key}: {value[0]} - Pollen Count: {value[1]}")

#  the area a bee is sent to
def check_area(hidden_field, visible_field, x, y, bee_type, flower_dict):
    pollen_harvested = 0

    if not (0 <= x < len(hidden_field) and 0 <= y < len(hidden_field[0])):
        print("Your bee has left the field and has been lost.")
        return pollen_harvested

    if hidden_field[x][y] == 'P':
        print("Your bee must have fallen into a pitcher plant and did not return.")
        return pollen_harvested

    for i in range(max(0, x - 1), min(len(hidden_field), x + 2)):
        
        for j in range(max(0, y - 1), min(len(hidden_field[0]), y + 2)):
            
            if bee_type == 'scout':
                if hidden_field[i][j] != 'H' and hidden_field[i][j] != ' ':
                    visible_field[i][j] = hidden_field[i][j]

            elif bee_type == 'worker':
                if hidden_field[i][j] == 'H':
                    continue

                elif hidden_field[i][j] == 'U':
                    continue

                elif hidden_field[i][j] == 'P':
                    print("Your bee must have fallen into a pitcher plant and did not return.")
                    return pollen_harvested
                
                elif hidden_field[i][j] != ' ':
                    pollen_harvested += flower_dict[hidden_field[i][j]][1]
                    hidden_field[i][j] = 'U'
    
    return pollen_harvested

