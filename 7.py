water_tank=255
num=int(input())
total_ltr=0
real_ltr=0
for i in range(num):
    ltr_watter=int(input())
    total_ltr+=ltr_watter
    if water_tank<total_ltr:
        total_ltr-=ltr_watter
        print("Insufficient capacity!")
        continue

print(total_ltr)
