number_lines=int(input())
open_br=0
close_br=0
is_balanced=False
last_str=0
for line in range(number_lines):

    input_str=input()

    if input_str=="(":
        open_br+=1
        last_str+=1
        if last_str==2:
            open_br-=1

    elif input_str==")":
        close_br+=1
        is_balanced=False
    else:
        last_str=0

    if open_br==close_br and open_br!=0:

            is_balanced=True
            open_br=0
            close_br=0

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


