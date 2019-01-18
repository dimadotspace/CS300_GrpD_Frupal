""" Map Configurations """
MAP_SIZE = 5

reference_map = [ ["҉"] * MAP_SIZE for i in range(MAP_SIZE) ]
        
island  = [ [0]* MAP_SIZE for i in range(MAP_SIZE) ]

""" Status of Hero """
coordinates = [[0],[0]]

def display():
    for i in range(0, MAP_SIZE):
        for j in range(0, MAP_SIZE):
            if i == coordinates[0][0] and j == coordinates[1][0]:
                print('웃', end =' ')
            elif abs(i - coordinates[0][0] ) < 2 and abs(j - coordinates[1][0]) < 2:
                                print(str(reference_map[i][j]), end = ' ')
            else:
                print(str(' '), end=' ')
        print("")
    

def controls():
    print("Please enter   w   to walk\n"
          + "             a s d\n"
          + "Press h for help\n"
          + "Press q to quit\n"
          + "Press x to display map")

def main():    
    print("""Welcome to the Game!""")

    controls()
    display()

    while True:
        choice = input("")

        if choice == 'q':
            break
        elif choice == 'x':
            display()
        elif choice == 'h':
            controls()

        #Walking South
        elif choice == 's': 
            if coordinates[0][0] < MAP_SIZE - 1:
                coordinates[0][0] = coordinates[0][0] + 1
            else:
                print("You have stepped on water!")
        #Walking North
        elif choice == 'w':
            if coordinates[0][0] > 0:
                coordinates[0][0] = coordinates[0][0] - 1 
            else:
                print("You have stepped on water!")
        #Walking East
        elif choice == 'a':
            if coordinates[1][0] > 0:
                coordinates[1][0] = coordinates[1][0] - 1
            else:
                print("You have stepped on water!")
        #Walking West
        elif choice == 'd':
            if coordinates[1][0] < MAP_SIZE - 1:
                coordinates[1][0] = coordinates[1][0] + 1
            else:
                print("You have stepped on water!")
        else:
            print("Try a valid command""")
            
        """ Update Status of Hero """
        """ Game Logic """
        
        display()
main()
