row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_int_column = int(position[0]) - 1
position_int_row = int(position[1]) - 1

map[position_int_row][position_int_column] = "X"





print(f"{row1}\n{row2}\n{row3}")