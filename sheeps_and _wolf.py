sheeps_and_wolf=input()

list_sheep=list(sheeps_and_wolf.split(", "))  # convert string to a list
list_sheep.reverse()
wolf=list_sheep.index("wolf",0, len(list_sheep))

if wolf!=0:
    print(f"Oi! Sheep number {wolf}! You are about to be eaten by a wolf!")
else:
    print("Please go away and stop eating my sheep")


