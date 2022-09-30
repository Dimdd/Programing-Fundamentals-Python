group_size=int(input())
days=int(input())
coins_earn=0
coins_spend=0
for current_day in range(1,days+1):

    coins_earn+=(50)
    coins_spend+=group_size*2
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 10 == 0:
        group_size -= 2

    if current_day%3==0:
        # coins_earn-=group_size*3
        coins_spend+=group_size*3

    if current_day%5==0:
        coins_earn+=20*group_size
        if current_day%3==0:
            coins_spend+=2*group_size


coins_earn=coins_earn-coins_spend
print(f"{group_size} companions received {int(coins_earn/group_size)} coins each.")



