import random

#defining map variables
map_size = 5
t_row = random.randint(0,map_size-1)
t_column = random.randint(0,map_size-1)

game_map = [["🏝" for i in range(map_size)]for i in range(map_size)]

def print_map():
  for row in game_map:
    print(" ").join(row)
    
  print()


print("Welcome to Treasure Island! You have been tasked with finding buried treausre on one of these islands!")

print_map()

while True:
  guess_row = int(input("Please enter the row of the island you want to search: ")) - 1
  guess_column = int(input("Please enter the column of the island you want to search: ")) - 1
  
  if guess_row < 0 or guess_row >= 5 or guess_column <0 or guess_column >= 5:
    print("Please enter a valid number between 1-5 inclusive:")
    
    continue
  
  if guess_row == t_row and guess_column == t_column:
    game_map[guess_row][guess_column] = "🪙"
    
    print_map()
    print("You successfully found the treausre! You win!")
    
    break
  else:
    if game_map[guess_row][guess_column] == "☠":
      print("You already searched there! Please search a new island!")
      
    else:
      game_map[guess_row][guess_column] = "☠"
      
      print("You found no treausre! Try searching a different island!")
      
      print_map()
