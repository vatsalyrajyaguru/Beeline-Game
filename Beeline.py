import BeeFunctions as bf

def main():
    try:
        flower_dict = bf.load_flower_list()
        hidden_field = bf.create_field(flower_dict)
        visible_field = bf.copy_field(hidden_field)

        num_scouts = 5
        num_workers = 5
        pollen_needed = 20
        pollen_harvested = 0

        bf.game_intro(flower_dict, num_scouts, num_workers, pollen_needed)

        while num_workers > 0 and pollen_harvested < pollen_needed:
            print("\nRemaining scout bees:", num_scouts)
            print("Remaining worker bees:", num_workers)
            print("Pollen harvested:", pollen_harvested)
            print("H: Hive, U: Used Flower\n")
            bf.print_field(visible_field)

            bee_type = input("Send a bee (S for scout, W for worker): ").upper()

            if bee_type == 'S':
                if num_scouts == 0:
                    print("No more scout bees remaining.")
                else:
                    x = int(input("Enter X coordinate: "))
                    y = int(input("Enter Y coordinate: "))
                    num_scouts -= 1
                    print("Sending out a scout...")
                    pollen_harvested += bf.check_area(hidden_field, visible_field, x, y, 'scout', flower_dict)
            elif bee_type == 'W':
                if num_workers == 0:
                    print("No more worker bees remaining.")
                else:
                    x = int(input("Enter X coordinate: "))
                    y = int(input("Enter Y coordinate: "))
                    num_workers -= 1
                    print("Sending out a worker...")
                    pollen_harvested += bf.check_area(hidden_field, visible_field, x, y, 'worker', flower_dict)
            else:
                print("Invalid bee type. Please choose either S or W.")

        if pollen_harvested >= pollen_needed:
            print("\nCongratulations! You have harvested enough pollen. You win!")
        else:
            print("\nSorry, you have run out of worker bees. You lose.")

    except TypeError as e:
        print(e)
        exit(-1)

if __name__ == "__main__":
    main()
