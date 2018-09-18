current_tile = 1.1

Travel_instructions = ""
while current_tile != 3.1:
    if current_tile == 1.1:
        print("You can travel: (N)orth.")
        direction = str(input("Direction: "))
        if direction == "N" or direction == "n":
            current_tile = 1.2
        else:
            print("Not a valid direction!")

    if current_tile == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = str((input("Direction: ")))
        if direction == "N" or direction == "n":
            current_tile = 1.3
        elif direction == "E" or direction == "e":
            current_tile = 2.2
        elif direction == "S" or direction == "s":
            cirrent_tile = 1.1
        else:
            print("Not a valid direction!")

    if current_tile == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        direction = str((input("Direction: ")))
        if direction == "E" or direction == "e":
            current_tile = 2.3
        elif direction == "S" or direction == "s":
            current_tile = 1.2
        else:
            print("Not a valid direction!")

    if current_tile == 2.3:
        print("You can travel: (W)est or (E)ast.")
        direction = str((input("Direction: ")))
        if direction == "W" or direction == "w":
            current_tile = 1.3
        elif direction == "E" or direction == "e":
            current_tile = 3.3
        else:
            print("Not a valid direction!")

    if current_tile == 2.2:
        print("You can travel: (W)est or (S)outh.")
        direction = str((input("Direction: ")))
        if direction == "W" or direction == "w":
            current_tile = 1.2
        elif direction == "S" or direction == "s":
            current_tile = 2.1
        else:
            print("Not a valid direction!")

    if current_tile == 2.1:
        print("You can travel: (N)orth.")
        direction = str((input("Direction: ")))
        if direction == "N" or direction == "n":
            current_tile = 2.2
        else:
            print("Not a valid direction!")


    if current_tile == 3.3:
        print("You can travel: (W)est or (S)outh.")
        direction = str((input("Direction: ")))
        if direction == "W" or direction == "w":
            current_tile = 2.3
        elif direction == "S" or direction == "s":
            current_tile = 3.2
        else:
            print("Not a valid direction!")

    if current_tile == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        direction = str((input("Direction: ")))
        if direction == "N" or direction == "n":
            current_tile = 3.3
        elif direction == "S" or direction == "s":
            current_tile = 3.1
            print("Victory!")
        else:
            print("Not a valid direction!")
