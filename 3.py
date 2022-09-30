num_people=int(input())
capacity_elevator=int(input())
number_lift=num_people//capacity_elevator
number_last=num_people%capacity_elevator
if number_last>0:
    number_lift+=1


print(number_lift)
