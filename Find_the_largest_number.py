input=int(input())

for a in range(1,input+1):


    if str(a)[0]+str(a)[1]=="5":

        print(f"{a}->True")
    else:
        print(f"{a}->False")