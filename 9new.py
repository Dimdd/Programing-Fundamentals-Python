number_snowballs=int(input())
snowball_value=0
lst=[]
for i in range(number_snowballs):

    snowball_weight=int(input())
    snowball_time=int(input())
    snowball_quality=int(input())


    snowball_value=int((snowball_weight / snowball_time) ** snowball_quality)
    lst.append([snowball_value,snowball_weight,snowball_quality,snowball_time])

lst.sort()
lst.reverse()

print(f"{lst[0][1]} : {lst[0][3]} = {lst[0][0]} ({lst[0][2]})")
